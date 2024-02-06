from typing import Any, Dict, List, Optional, Tuple

import requests

from movie_schedules.constants.cinepolis import (
    CINEMA_CITIES, CINEMA_ZONES, CINEMAS, CINEMAS_SANTIAGO,
    NORTE_Y_CENTRO_DE_CHILE_TAGS, SANTIAGO_CENTRO_TAGS,
    SANTIAGO_NORTE_Y_PONIENTE_TAGS, SANTIAGO_ORIENTE_TAGS, SANTIAGO_SUR_TAGS,
    SUR_DE_CHILE_TAGS)
from movie_schedules.constants.main import ESP, SUB, TD_ESP, TD_SUB
from movie_schedules.dataclasses.cinema import Cinema, ShowDate
from movie_schedules.dataclasses.movie import Movie, ShowTime
from movie_schedules.services.main import CinemaService


class CinepolisService(CinemaService):
    name = ""
    host = "https://cinepolischile.cl"

    def get_cinemas_from_zone(self, zone_name: str) -> List[str]:
        for cinema_zone in CINEMA_ZONES:
            if zone_name == cinema_zone["tag"]:
                return cinema_zone["list"]
        return []

    def get_zone_by_cinema(self, cinema: str) -> Optional[str]:
        if cinema in NORTE_Y_CENTRO_DE_CHILE_TAGS:
            return "norte-y-centro-de-chile"
        elif cinema in SANTIAGO_CENTRO_TAGS:
            return "santiago-centro"
        elif cinema in SANTIAGO_ORIENTE_TAGS:
            return "santiago-oriente"
        elif cinema in SANTIAGO_NORTE_Y_PONIENTE_TAGS:
            return "santiago-poniente-y-norte"
        elif cinema in SANTIAGO_SUR_TAGS:
            return "santiago-sur"
        elif cinema in SUR_DE_CHILE_TAGS:
            return "sur-de-chile"
        return None

    def is_chain(self, cinema: str) -> bool:
        zone = self.get_zone_by_cinema(cinema)
        return zone is not None

    def get_showings_response_by_zone(
        self,
        zone: str = "santiago-oriente",
    ) -> List[Dict[str, Any]]:
        try:
            payload = {"claveCiudad": zone, "esVIP": False}
            showings = requests.post(
                f"{self.host}/Cartelera.aspx/GetNowPlayingByCity", json=payload
            )
            clean_showings = showings.json()
            return clean_showings["d"]["Cinemas"]
        except Exception:
            return []

    def get_cinemas_by_zone(self, zone: str) -> List[Dict[str, Any]]:
        for cinema_zone in CINEMA_ZONES:
            if cinema_zone["tag"] == zone:
                return cinema_zone["list"]
        return []

    def get_only_showings_from_cinemas(
        self, cinema_showings: List[Dict[str, Any]], cinemas: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        reduced_cinema_showings = []
        for cinema_showing in cinema_showings:
            for cinema in cinemas:
                if cinema_showing["Key"] == cinema["id"]:
                    reduced_cinema_showings.append(cinema_showing)
        return reduced_cinema_showings

    def get_cinema_by_cinema_key(self, cinema_name: str) -> Optional[Dict[str, Any]]:
        for zone in CINEMA_ZONES:
            cinemas_in_zone = zone["list"]
            for cinema in cinemas_in_zone:
                if cinema_name == cinema["tag"]:
                    return cinema
        return None

    def get_cinema_by_cinemas_and_cinema_key(
        self, cinemas: List[Dict[str, Any]], cinema_key: str
    ) -> Dict[str, Any]:
        for cinema in cinemas:
            if cinema["Key"] == cinema_key:
                return cinema
        return {}

    def get_showtimes_by_date(
        self, cinemas: Dict[str, Any], date_name: str
    ) -> Dict[str, Any]:
        for date in cinemas["Dates"]:
            formatted_showing_date = date["ShowtimeDate"].replace(" ", "-")
            day, month = formatted_showing_date.split("-")
            if int(day) < 10 and len(day) == 2:
                formatted_showing_date = formatted_showing_date[1:]
            formatted_searched_date = date_name.replace(" ", "-")
            if formatted_showing_date == formatted_searched_date:
                return date
        return {}

    def get_movie_showings(
        self, movie_list: List[Dict[str, Any]], movie_title="batman"
    ) -> Dict:
        for movie in movie_list:
            if movie_title in movie["Key"] or movie["Key"] in movie_title:
                return movie
        return {}

    def get_formatted_format(self, format: str):
        if format == "ESP":
            return "2D ESP"
        if format == "SUBT":
            return "2D SUB"
        format = format.replace("DOB", "ESP")
        format = format.replace("SUBT", "SUB")
        return format

    def get_showtimes(self, movie_showings: Dict, format: str = None) -> List[ShowTime]:
        total_showtimes = []
        for formats in movie_showings["Formats"]:
            showtimes = formats["Showtimes"]
            format_name = self.get_formatted_format(formats["Name"])
            if format and format not in format_name:
                continue
            for show in showtimes:
                showtime = show["Time"]
                total_showtimes.append(
                    ShowTime(showtime=showtime, format=format_name, seats="")
                )
        return total_showtimes

    def get_showings(
        self, movie: str, date: str, cinema: str, format: str
    ) -> Optional[ShowDate]:
        zone = self.get_zone_by_cinema(cinema)
        cinema_showings = self.get_cinema_by_cinemas_and_cinema_key(
            self.get_showings_response_by_zone(zone), cinema
        )
        if not cinema_showings:
            return None
        cinema_name = cinema_showings["Name"]
        showtime_date = self.get_showtimes_by_date(cinema_showings, date)
        showtime_date_name = showtime_date["ShowtimeDate"]
        showtime_movies = showtime_date["Movies"]
        movie_showings = self.get_movie_showings(showtime_movies, movie)
        movie_title = movie_showings["Title"]
        showdate = ShowDate(
            date=showtime_date_name,
            cinemas=[
                Cinema(
                    name=cinema_name,
                    movies=[
                        Movie(
                            title=movie_title,
                            showtimes=self.get_showtimes(movie_showings, format),
                        )
                    ],
                )
            ],
        )
        return showdate

    def get_formatted_showings_by_cinema(
        self,
        date: str,
        cinema_key: str,
        zone_showings: List[Dict[str, Any]],
        movie: str,
        format: str,
    ) -> Optional[Cinema]:
        cinema = self.get_cinema_by_cinemas_and_cinema_key(zone_showings, cinema_key)
        if not cinema:
            return None
        showtime_date = self.get_showtimes_by_date(cinema, date.replace("-", " "))
        if not showtime_date:
            return None
        movies = []
        for movie_showing in showtime_date["Movies"]:
            if not movie or (
                movie in movie_showing["Key"] or movie_showing["Key"] in movie
            ):
                movies.append(
                    Movie(
                        title=movie_showing["Title"],
                        showtimes=self.get_showtimes(movie_showing, format),
                    )
                )
        cinema_showtimes = Cinema(name=cinema["Name"], movies=movies)
        return cinema_showtimes

    def get_formatted_showings_by_zone(
        self, date: str, zone: str, movie: str, format: str
    ) -> List[Cinema]:
        if zone not in CINEMAS:
            return []
        zone_showings = self.get_showings_response_by_zone(zone)
        cinemas_in_zone = CINEMAS[zone]
        zone_showtimes = []
        for cinema in cinemas_in_zone["list"]:
            zone_showtime = self.get_formatted_showings_by_cinema(
                date, cinema["tag"], zone_showings, movie, format
            )
            if not zone_showtime:
                continue
            zone_showtimes.append(zone_showtime)
        return zone_showtimes

    def get_zones(self, zone_name: str) -> Tuple[List[str], bool]:
        is_city = False
        if zone_name == "santiago":
            zones = CINEMAS_SANTIAGO
        elif zone_name in CINEMA_CITIES.keys():
            is_city = True
            zones = [CINEMA_CITIES[zone_name]]
        else:
            zones = [zone_name]
        return zones, is_city

    def get_zone_showings(
        self, zone: str, zone_name: str, is_city: bool
    ) -> List[Dict[str, Any]]:
        zone_showings = self.get_showings_response_by_zone(zone)
        if is_city:
            zone_showings = self.get_only_showings_from_cinemas(
                zone_showings, self.get_cinemas_by_zone(zone_name)
            )
        return zone_showings

    def get_showings_by_zone(
        self, movie: str, date: str, zone_name: str, format: str
    ) -> List[Cinema]:
        zones, is_city = self.get_zones(zone_name)
        cinema_showtimes = []
        for zone in zones:
            zone_showings = self.get_zone_showings(zone, zone_name, is_city)
            for cinema in zone_showings:
                cinema_showtime = self.get_formatted_showings_by_cinema(
                    date, cinema["Key"], zone_showings, movie, format
                )
                if not cinema_showtime:
                    continue
                cinema_showtimes.append(cinema_showtime)
        return cinema_showtimes

    def get_showing_by_date(self, movie: str, date: str, format: str) -> List[Cinema]:
        cinema_showtimes = []
        for zone in CINEMAS:
            cinema_showtime = self.get_formatted_showings_by_zone(
                date, zone, movie, format
            )
            if not cinema_showtime:
                continue
            cinema_showtimes += cinema_showtime
        return cinema_showtimes

    def get_showdate_from_showtime_date(
        self, showtime_date: Dict[str, Any], movie: str, cinema_name: str, format: str
    ) -> Optional[ShowDate]:
        showtime_date_name = showtime_date["ShowtimeDate"]
        showtime_movies = showtime_date["Movies"]
        movie_showings = self.get_movie_showings(showtime_movies, movie)
        if not movie_showings:
            return
        movie_title = movie_showings["Title"]
        return ShowDate(
            date=showtime_date_name,
            cinemas=[
                Cinema(
                    name=cinema_name,
                    movies=[
                        Movie(
                            title=movie_title,
                            showtimes=self.get_showtimes(movie_showings, format),
                        )
                    ],
                )
            ],
        )

    def get_showing_by_cinema(
        self, movie: str, cinema: str, format: str = None
    ) -> List[ShowDate]:
        zone = self.get_zone_by_cinema(cinema)
        cinema_showings = self.get_cinema_by_cinemas_and_cinema_key(
            self.get_showings_response_by_zone(zone), cinema
        )
        cinema_name = cinema_showings["Name"]
        cinema_dates = cinema_showings["Dates"]
        total_showings = []
        for showtime_date in cinema_dates:
            showdate = self.get_showdate_from_showtime_date(
                showtime_date, movie, cinema_name, format
            )
            if showdate:
                total_showings.append(showdate)
        return total_showings

    def get_showing_by_zone(
        self, movie: str, zone_name: str, format: str = None
    ) -> List[ShowDate]:
        zones, is_city = self.get_zones(zone_name)
        total_showings = []
        for zone in zones:
            zone_showings = self.get_zone_showings(zone, zone_name, is_city)
            for cinema_showings in zone_showings:
                cinema_name = cinema_showings["Name"]
                cinema_dates = cinema_showings["Dates"]
                total_showings = []
                for showtime_date in cinema_dates:
                    showdate = self.get_showdate_from_showtime_date(
                        showtime_date, movie, cinema_name, format
                    )
                    if showdate:
                        total_showings.append(showdate)
        return total_showings

    def get_movie_showtimes(
        self, showtime_movies: List[Dict[str, Any]], format: str
    ) -> List[Movie]:
        movies = []
        for movie_showings in showtime_movies:
            movie_title = movie_showings["Title"]
            movies.append(
                Movie(
                    title=movie_title,
                    showtimes=self.get_showtimes(movie_showings, format),
                )
            )
        return movies

    def get_cinema_showings(self, cinema: str, format: str) -> List[ShowDate]:
        zone = self.get_zone_by_cinema(cinema)
        cinema_showings = self.get_cinema_by_cinemas_and_cinema_key(
            self.get_showings_response_by_zone(zone), cinema
        )
        cinema_name = cinema_showings["Name"]
        cinema_dates = cinema_showings["Dates"]
        total_showings = []
        for showtime_date in cinema_dates:
            showtime_date_name = showtime_date["ShowtimeDate"]
            movies = self.get_movie_showtimes(showtime_date["Movies"], format)
            total_showings.append(
                ShowDate(
                    date=showtime_date_name,
                    cinemas=[Cinema(name=cinema_name, movies=movies)],
                )
            )
        return total_showings

    def get_cinema_showings_by_zone(
        self, zone_name: str, format: str
    ) -> List[ShowDate]:
        zones, is_city = self.get_zones(zone_name)
        total_showings = []
        for zone in zones:
            zone_showings = self.get_zone_showings(zone, zone_name, is_city)
            for cinema_showings in zone_showings:
                cinema_name = cinema_showings["Name"]
                cinema_dates = cinema_showings["Dates"]
                for showtime_date in cinema_dates:
                    showtime_date_name = showtime_date["ShowtimeDate"]
                    movies = self.get_movie_showtimes(showtime_date["Movies"], format)
                    total_showings.append(
                        ShowDate(
                            date=showtime_date_name,
                            cinemas=[Cinema(name=cinema_name, movies=movies)],
                        )
                    )
        return total_showings

    def get_cinema_showings_by_date(
        self, cinema: str, date: str, format: str
    ) -> ShowDate:
        zone = self.get_zone_by_cinema(cinema)
        cinema_showings = self.get_cinema_by_cinemas_and_cinema_key(
            self.get_showings_response_by_zone(zone), cinema
        )
        cinema_name = cinema_showings["Name"]
        showtime_date = self.get_showtimes_by_date(
            cinema_showings, date.replace("-", " ")
        )
        showtime_date_name = showtime_date["ShowtimeDate"]
        movies = self.get_movie_showtimes(showtime_date["Movies"], format)
        return ShowDate(
            date=showtime_date_name, cinemas=([Cinema(name=cinema_name, movies=movies)])
        )

    def get_cinema_showings_by_date_and_zone(
        self, zone_name: str, date: str, format: str
    ) -> List[ShowDate]:
        zones, is_city = self.get_zones(zone_name)
        total_showings = []
        for zone in zones:
            zone_showings = self.get_zone_showings(zone, zone_name, is_city)
            for cinema_showing in zone_showings:
                cinema_name = cinema_showing["Name"]
                showtime_date = self.get_showtimes_by_date(
                    cinema_showing, date.replace("-", " ")
                )
                showtime_date_name = showtime_date["ShowtimeDate"]
                movies = self.get_movie_showtimes(showtime_date["Movies"], format)
                total_showings.append(
                    ShowDate(
                        date=showtime_date_name,
                        cinemas=([Cinema(name=cinema_name, movies=movies)]),
                    )
                )
        return total_showings

    def get_total(self, date: str, format: str) -> List[Cinema]:
        cinema_showtimes = []
        for zone in CINEMAS:
            cinema_showtime = self.get_formatted_showings_by_zone(
                date, zone, "", format
            )
            if not cinema_showtime:
                continue
            cinema_showtimes += cinema_showtime
        return cinema_showtimes
