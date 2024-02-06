import asyncio
import logging
import time
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Process
from threading import Thread

import discord
from decouple import config
from discord.ext import commands
from flask import Flask, render_template
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from movie_schedules.services.bot import CinemaBot

asyncio.set_event_loop(asyncio.new_event_loop())


app = Flask(__name__)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="$m.", intents=intents)

cinema_bot = CinemaBot()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_args(*args):
    cinema = None
    date = None
    movie = None
    format = None
    mode = None
    for arg in args:
        if arg.startswith("fecha=") or arg.startswith("f="):
            date = arg.split("=")[1]
        if arg.startswith("pelicula=") or arg.startswith("p="):
            movie = arg.split("=")[1]
        if arg.startswith("cine=") or arg.startswith("c="):
            cinema = arg.split("=")[1]
        if arg.startswith("formato=") or arg.startswith("fm="):
            format = arg.split("=")[1]
        if arg.startswith("modo=") or arg.startswith("m="):
            mode = arg.split("=")[1]
    return cinema, date, movie, format, mode


@app.route("/")
def home():
    return render_template("home.html")


@bot.event
async def on_ready():
    print("Bot has been connected!")


@bot.command()
async def ping(ctx):
    await ctx.send("pong")


@bot.command()
async def horarios(ctx, *args):
    logger.info("Procesando horarios!")
    cinema, date, movie, format, mode = get_args(*args)

    if not movie and date and cinema:
        message, total = cinema_bot.get_general_cinema_showings(cinema, date, format)
    elif movie and not date and cinema:
        message, total = cinema_bot.get_movie_date_message(
            bot.get_showing_by_cinema(movie, cinema, format), "CINEMA"
        )
    else:
        message, total = cinema_bot.get_general_showings(movie, date, cinema, format)
    message = f"{total} HORARIOS EN TOTAL \n——————\n{message}"
    for cinema_showing_part in message.split("$SEPARATOR$"):
        if cinema_showing_part and cinema_showing_part not in ("\n", "\n\n"):
            await ctx.send(cinema_showing_part)


@bot.command()
async def total(ctx, *args):
    logger.info("Procesando total!")
    _, date, _, format, mode = get_args(*args)

    if mode == "debug":
        await ctx.send("Comando recibido!")
        time_start = time.time()
    message = cinema_bot.get_total(date, format)
    await ctx.send(message)
    if mode == "debug":
        delta_time = time.time() - time_start
        await ctx.send(f"Comando finalizado en {int(delta_time)} segundos")


@bot.command()
async def total_formatos(ctx, *args):
    logger.info("Procesando total formatos!")
    _, date, _, format, mode = get_args(*args)
    message = cinema_bot.get_format_total(date, format)
    await ctx.send(message)


@bot.command()
async def total_cinemas(ctx, *args):
    logger.info("Procesando total cinemas!")
    _, date, _, format = get_args(args)
    message = cinema_bot.get_cinema_total(date, format)
    await ctx.send(message)


@bot.command()
async def info_cities(ctx):
    cities = cinema_bot.get_info_cities()
    await ctx.send(cities)


@bot.command()
async def info_cinemas(ctx):
    cinemas = cinema_bot.get_info_cinemas()
    await ctx.send(cinemas)


@bot.command()
async def info(ctx):
    info = "$c.horarios nombre-pelicula fecha nombre-cine(opcional)\nHORARIOS PELÍCULA PARA UNA FECHA EN PARTICULAR. EN UN CINE O TODOS LOS CINES. NOMBRE DEL CINE TAMBIÉN PUEDE SER UNA ZONA.\n\n"
    info += "$c.total fecha\nRECUENTO DE PELÍCULAS TOTALES POR FECHA.\n\n"
    info += "$c.info_cities\nLISTA DE ZONAS INCLUIDAS.\n\n"
    info += "$c.info_cinemas\nLISTA DE CINES INCLUIDOS.\n\n"
    await ctx.send(info)


if __name__ == "__main__":
    bot.run(config("DISCORD_TOKEN"))
