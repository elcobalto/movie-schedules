import json

from movie_schedules.dataclasses.cinema import Cinema, ShowDate
from movie_schedules.dataclasses.movie import Movie, ShowTime

with open("tests/fixtures/cinemark_fixture.json") as f:
    cinemark_fixture = json.load(f)

wonka_february_showings_fixture = [
    Cinema(
        name="Cinemark MallPlaza Arica",
        movies=[
            Movie(
                title="wonka",
                showtimes=[
                    ShowTime(showtime="13:20", format="2D ESP", seats=112),
                    ShowTime(showtime="16:00", format="2D ESP", seats=109),
                ],
            )
        ],
    ),
    Cinema(
        name="Cinemark MallPlaza Iquique",
        movies=[
            Movie(
                title="wonka",
                showtimes=[
                    ShowTime(showtime="13:20", format="2D ESP", seats=112),
                    ShowTime(showtime="16:00", format="2D ESP", seats=109),
                ],
            )
        ],
    ),
    Cinema(
        name="Cinemark MallPlaza La Serena",
        movies=[
            Movie(
                title="wonka",
                showtimes=[
                    ShowTime(showtime="13:20", format="2D ESP", seats=112),
                    ShowTime(showtime="16:00", format="2D ESP", seats=109),
                ],
            )
        ],
    ),
    Cinema(
        name="Cinemark Open Ovalle",
        movies=[
            Movie(
                title="wonka",
                showtimes=[
                    ShowTime(showtime="13:20", format="2D ESP", seats=112),
                    ShowTime(showtime="16:00", format="2D ESP", seats=109),
                ],
            )
        ],
    ),
    Cinema(
        name="Cinemark Open La Calera",
        movies=[
            Movie(
                title="wonka",
                showtimes=[
                    ShowTime(showtime="13:20", format="2D ESP", seats=112),
                    ShowTime(showtime="16:00", format="2D ESP", seats=109),
                ],
            )
        ],
    ),
    Cinema(
        name="Cinemark Espacio Urbano",
        movies=[
            Movie(
                title="wonka",
                showtimes=[
                    ShowTime(showtime="13:20", format="2D ESP", seats=112),
                    ShowTime(showtime="16:00", format="2D ESP", seats=109),
                ],
            )
        ],
    ),
    Cinema(
        name="Cinemark MallMarina",
        movies=[
            Movie(
                title="wonka",
                showtimes=[
                    ShowTime(showtime="13:20", format="2D ESP", seats=112),
                    ShowTime(showtime="16:00", format="2D ESP", seats=109),
                ],
            )
        ],
    ),
    Cinema(
        name="Cinemark Alto las Condes",
        movies=[
            Movie(
                title="wonka",
                showtimes=[
                    ShowTime(showtime="13:20", format="2D ESP", seats=112),
                    ShowTime(showtime="16:00", format="2D ESP", seats=109),
                ],
            )
        ],
    ),
    Cinema(
        name="Cinemark Portal Ñuñoa",
        movies=[
            Movie(
                title="wonka",
                showtimes=[
                    ShowTime(showtime="13:20", format="2D ESP", seats=112),
                    ShowTime(showtime="16:00", format="2D ESP", seats=109),
                ],
            )
        ],
    ),
    Cinema(
        name="Cinemark MallPlaza Norte",
        movies=[
            Movie(
                title="wonka",
                showtimes=[
                    ShowTime(showtime="13:20", format="2D ESP", seats=112),
                    ShowTime(showtime="16:00", format="2D ESP", seats=109),
                ],
            )
        ],
    ),
    Cinema(
        name="Cinemark MallPlaza Oeste",
        movies=[
            Movie(
                title="wonka",
                showtimes=[
                    ShowTime(showtime="13:20", format="2D ESP", seats=112),
                    ShowTime(showtime="16:00", format="2D ESP", seats=109),
                ],
            )
        ],
    ),
    Cinema(
        name="Cinemark Mid Mall Maipú",
        movies=[
            Movie(
                title="wonka",
                showtimes=[
                    ShowTime(showtime="13:20", format="2D ESP", seats=112),
                    ShowTime(showtime="16:00", format="2D ESP", seats=109),
                ],
            )
        ],
    ),
    Cinema(
        name="Cinemark MallPlaza Tobalaba",
        movies=[
            Movie(
                title="wonka",
                showtimes=[
                    ShowTime(showtime="13:20", format="2D ESP", seats=112),
                    ShowTime(showtime="16:00", format="2D ESP", seats=109),
                ],
            )
        ],
    ),
    Cinema(
        name="Cinemark MallPlaza Vespucio",
        movies=[
            Movie(
                title="wonka",
                showtimes=[
                    ShowTime(showtime="13:20", format="2D ESP", seats=112),
                    ShowTime(showtime="16:00", format="2D ESP", seats=109),
                ],
            )
        ],
    ),
    Cinema(
        name="Cinemark Open Rancagua",
        movies=[
            Movie(
                title="wonka",
                showtimes=[
                    ShowTime(showtime="13:20", format="2D ESP", seats=112),
                    ShowTime(showtime="16:00", format="2D ESP", seats=109),
                ],
            )
        ],
    ),
    Cinema(
        name="Cinemark Mall Rancagua",
        movies=[
            Movie(
                title="wonka",
                showtimes=[
                    ShowTime(showtime="13:20", format="2D ESP", seats=112),
                    ShowTime(showtime="16:00", format="2D ESP", seats=109),
                ],
            )
        ],
    ),
    Cinema(
        name="Cinemark MallPlaza Trebol",
        movies=[
            Movie(
                title="wonka",
                showtimes=[
                    ShowTime(showtime="13:20", format="2D ESP", seats=112),
                    ShowTime(showtime="16:00", format="2D ESP", seats=109),
                ],
            )
        ],
    ),
    Cinema(
        name="Cinemark MallPlaza Mirador Bio-Bio",
        movies=[
            Movie(
                title="wonka",
                showtimes=[
                    ShowTime(showtime="13:20", format="2D ESP", seats=112),
                    ShowTime(showtime="16:00", format="2D ESP", seats=109),
                ],
            )
        ],
    ),
    Cinema(
        name="Cinemark Arauco Coronel",
        movies=[
            Movie(
                title="wonka",
                showtimes=[
                    ShowTime(showtime="13:20", format="2D ESP", seats=112),
                    ShowTime(showtime="16:00", format="2D ESP", seats=109),
                ],
            )
        ],
    ),
    Cinema(
        name="Cinemark Portal Osorno",
        movies=[
            Movie(
                title="wonka",
                showtimes=[
                    ShowTime(showtime="13:20", format="2D ESP", seats=112),
                    ShowTime(showtime="16:00", format="2D ESP", seats=109),
                ],
            )
        ],
    ),
]

mallplaza_airca_wonka_showings_fixture = [
    ShowDate(
        date="2024-02-04",
        cinemas=[
            Cinema(
                name="cinemark-mallplaza-arica",
                movies=[
                    Movie(
                        title="wonka",
                        showtimes=[
                            ShowTime(showtime="13:20", format="2D ESP", seats=112),
                            ShowTime(showtime="16:00", format="2D ESP", seats=109),
                        ],
                    )
                ],
            )
        ],
    ),
    ShowDate(
        date="2024-02-05",
        cinemas=[
            Cinema(
                name="cinemark-mallplaza-arica",
                movies=[
                    Movie(
                        title="wonka",
                        showtimes=[
                            ShowTime(showtime="10:40", format="2D ESP", seats=112),
                            ShowTime(showtime="13:20", format="2D ESP", seats=112),
                        ],
                    )
                ],
            )
        ],
    ),
    ShowDate(
        date="2024-02-06",
        cinemas=[
            Cinema(
                name="cinemark-mallplaza-arica",
                movies=[
                    Movie(
                        title="wonka",
                        showtimes=[
                            ShowTime(showtime="10:40", format="2D ESP", seats=112),
                            ShowTime(showtime="13:20", format="2D ESP", seats=112),
                            ShowTime(showtime="16:00", format="2D ESP", seats=112),
                        ],
                    )
                ],
            )
        ],
    ),
    ShowDate(
        date="2024-02-07",
        cinemas=[
            Cinema(
                name="cinemark-mallplaza-arica",
                movies=[
                    Movie(
                        title="wonka",
                        showtimes=[
                            ShowTime(showtime="10:40", format="2D ESP", seats=112),
                            ShowTime(showtime="13:20", format="2D ESP", seats=112),
                            ShowTime(showtime="16:00", format="2D ESP", seats=112),
                        ],
                    )
                ],
            )
        ],
    ),
    ShowDate(
        date="2024-02-22", cinemas=[Cinema(name="cinemark-mallplaza-arica", movies=[])]
    ),
    ShowDate(
        date="2024-02-23", cinemas=[Cinema(name="cinemark-mallplaza-arica", movies=[])]
    ),
    ShowDate(
        date="2024-02-24", cinemas=[Cinema(name="cinemark-mallplaza-arica", movies=[])]
    ),
    ShowDate(
        date="2024-02-25", cinemas=[Cinema(name="cinemark-mallplaza-arica", movies=[])]
    ),
    ShowDate(
        date="2024-02-26", cinemas=[Cinema(name="cinemark-mallplaza-arica", movies=[])]
    ),
    ShowDate(
        date="2024-02-27", cinemas=[Cinema(name="cinemark-mallplaza-arica", movies=[])]
    ),
    ShowDate(
        date="2024-02-28", cinemas=[Cinema(name="cinemark-mallplaza-arica", movies=[])]
    ),
]

arica_wonka_showings_fixture = [
    ShowDate(
        date="2024-02-04",
        cinemas=[
            Cinema(
                name="Cinemark MallPlaza Arica",
                movies=[
                    Movie(
                        title="wonka",
                        showtimes=[
                            ShowTime(showtime="13:20", format="2D ESP", seats=112),
                            ShowTime(showtime="16:00", format="2D ESP", seats=109),
                        ],
                    )
                ],
            )
        ],
    ),
    ShowDate(
        date="2024-02-05",
        cinemas=[
            Cinema(
                name="Cinemark MallPlaza Arica",
                movies=[
                    Movie(
                        title="wonka",
                        showtimes=[
                            ShowTime(showtime="10:40", format="2D ESP", seats=112),
                            ShowTime(showtime="13:20", format="2D ESP", seats=112),
                        ],
                    )
                ],
            )
        ],
    ),
    ShowDate(
        date="2024-02-06",
        cinemas=[
            Cinema(
                name="Cinemark MallPlaza Arica",
                movies=[
                    Movie(
                        title="wonka",
                        showtimes=[
                            ShowTime(showtime="10:40", format="2D ESP", seats=112),
                            ShowTime(showtime="13:20", format="2D ESP", seats=112),
                            ShowTime(showtime="16:00", format="2D ESP", seats=112),
                        ],
                    )
                ],
            )
        ],
    ),
    ShowDate(
        date="2024-02-07",
        cinemas=[
            Cinema(
                name="Cinemark MallPlaza Arica",
                movies=[
                    Movie(
                        title="wonka",
                        showtimes=[
                            ShowTime(showtime="10:40", format="2D ESP", seats=112),
                            ShowTime(showtime="13:20", format="2D ESP", seats=112),
                            ShowTime(showtime="16:00", format="2D ESP", seats=112),
                        ],
                    )
                ],
            )
        ],
    ),
    ShowDate(
        date="2024-02-22", cinemas=[Cinema(name="Cinemark MallPlaza Arica", movies=[])]
    ),
    ShowDate(
        date="2024-02-23", cinemas=[Cinema(name="Cinemark MallPlaza Arica", movies=[])]
    ),
    ShowDate(
        date="2024-02-24", cinemas=[Cinema(name="Cinemark MallPlaza Arica", movies=[])]
    ),
    ShowDate(
        date="2024-02-25", cinemas=[Cinema(name="Cinemark MallPlaza Arica", movies=[])]
    ),
    ShowDate(
        date="2024-02-26", cinemas=[Cinema(name="Cinemark MallPlaza Arica", movies=[])]
    ),
    ShowDate(
        date="2024-02-27", cinemas=[Cinema(name="Cinemark MallPlaza Arica", movies=[])]
    ),
    ShowDate(
        date="2024-02-28", cinemas=[Cinema(name="Cinemark MallPlaza Arica", movies=[])]
    ),
]

mallplaza_arica_movie_showtimes = [
    Movie(title="wonka", showtimes=[]),
    Movie(title="patos", showtimes=[]),
    Movie(title="wish", showtimes=[]),
    Movie(
        title="los-colonos",
        showtimes=[ShowTime(showtime="22:20", format="2D SUB", seats=174)],
    ),
    Movie(
        title="con-todos-menos-contigo",
        showtimes=[ShowTime(showtime="21:50", format="2D SUB", seats=182)],
    ),
    Movie(
        title="pobres-criaturas",
        showtimes=[
            ShowTime(showtime="11:50", format="2D SUB", seats=254),
            ShowTime(showtime="15:00", format="2D SUB", seats=240),
            ShowTime(showtime="18:10", format="2D SUB", seats=227),
            ShowTime(showtime="21:30", format="2D SUB", seats=256),
        ],
    ),
    Movie(title="masha-y-el-oso", showtimes=[]),
    Movie(
        title="el-niño-y-la-garza",
        showtimes=[ShowTime(showtime="19:00", format="2D SUB", seats=170)],
    ),
    Movie(
        title="argylle:-agente-secreto",
        showtimes=[ShowTime(showtime="22:30", format="2D SUB", seats=170)],
    ),
    Movie(
        title="chicas-pesadas",
        showtimes=[
            ShowTime(showtime="19:10", format="2D SUB", seats=116),
            ShowTime(showtime="22:00", format="2D SUB", seats=122),
        ],
    ),
    Movie(
        title="vidas-pasadas",
        showtimes=[
            ShowTime(showtime="18:40", format="2D SUB", seats=148),
            ShowTime(showtime="21:20", format="2D SUB", seats=167),
        ],
    ),
    Movie(
        title="anatomía-de-una-caída",
        showtimes=[
            ShowTime(showtime="18:50", format="2D SUB", seats=108),
            ShowTime(showtime="22:10", format="2D SUB", seats=112),
        ],
    ),
]

mallplaza_arica_showdates_fixture = [
    ShowDate(
        date="2024-02-04",
        cinemas=[
            Cinema(
                name="cinemark-mallplaza-arica",
                movies=[
                    Movie(title="wonka", showtimes=[]),
                    Movie(title="patos", showtimes=[]),
                    Movie(title="wish", showtimes=[]),
                    Movie(
                        title="los-colonos",
                        showtimes=[
                            ShowTime(showtime="22:20", format="2D SUB", seats=174)
                        ],
                    ),
                    Movie(
                        title="con-todos-menos-contigo",
                        showtimes=[
                            ShowTime(showtime="21:50", format="2D SUB", seats=182)
                        ],
                    ),
                    Movie(
                        title="pobres-criaturas",
                        showtimes=[
                            ShowTime(showtime="11:50", format="2D SUB", seats=254),
                            ShowTime(showtime="15:00", format="2D SUB", seats=240),
                            ShowTime(showtime="18:10", format="2D SUB", seats=227),
                            ShowTime(showtime="21:30", format="2D SUB", seats=256),
                        ],
                    ),
                    Movie(title="masha-y-el-oso", showtimes=[]),
                    Movie(
                        title="el-niño-y-la-garza",
                        showtimes=[
                            ShowTime(showtime="19:00", format="2D SUB", seats=170)
                        ],
                    ),
                    Movie(
                        title="argylle:-agente-secreto",
                        showtimes=[
                            ShowTime(showtime="22:30", format="2D SUB", seats=170)
                        ],
                    ),
                    Movie(
                        title="chicas-pesadas",
                        showtimes=[
                            ShowTime(showtime="19:10", format="2D SUB", seats=116),
                            ShowTime(showtime="22:00", format="2D SUB", seats=122),
                        ],
                    ),
                    Movie(
                        title="vidas-pasadas",
                        showtimes=[
                            ShowTime(showtime="18:40", format="2D SUB", seats=148),
                            ShowTime(showtime="21:20", format="2D SUB", seats=167),
                        ],
                    ),
                    Movie(
                        title="anatomía-de-una-caída",
                        showtimes=[
                            ShowTime(showtime="18:50", format="2D SUB", seats=108),
                            ShowTime(showtime="22:10", format="2D SUB", seats=112),
                        ],
                    ),
                ],
            )
        ],
    ),
    ShowDate(
        date="2024-02-05",
        cinemas=[
            Cinema(
                name="cinemark-mallplaza-arica",
                movies=[
                    Movie(title="wonka", showtimes=[]),
                    Movie(title="patos", showtimes=[]),
                    Movie(title="wish", showtimes=[]),
                    Movie(
                        title="los-colonos",
                        showtimes=[
                            ShowTime(showtime="22:20", format="2D SUB", seats=172)
                        ],
                    ),
                    Movie(
                        title="con-todos-menos-contigo",
                        showtimes=[
                            ShowTime(showtime="21:50", format="2D SUB", seats=191)
                        ],
                    ),
                    Movie(
                        title="pobres-criaturas",
                        showtimes=[
                            ShowTime(showtime="11:50", format="2D SUB", seats=263),
                            ShowTime(showtime="15:00", format="2D SUB", seats=263),
                            ShowTime(showtime="18:10", format="2D SUB", seats=263),
                            ShowTime(showtime="21:30", format="2D SUB", seats=261),
                        ],
                    ),
                    Movie(title="masha-y-el-oso", showtimes=[]),
                    Movie(
                        title="el-niño-y-la-garza",
                        showtimes=[
                            ShowTime(showtime="19:00", format="2D SUB", seats=191)
                        ],
                    ),
                    Movie(
                        title="argylle:-agente-secreto",
                        showtimes=[
                            ShowTime(showtime="22:30", format="2D SUB", seats=170)
                        ],
                    ),
                    Movie(
                        title="chicas-pesadas",
                        showtimes=[
                            ShowTime(showtime="19:10", format="2D SUB", seats=118),
                            ShowTime(showtime="22:00", format="2D SUB", seats=122),
                        ],
                    ),
                    Movie(
                        title="callas-paris-1958",
                        showtimes=[
                            ShowTime(showtime="16:00", format="2D SUB", seats=104)
                        ],
                    ),
                    Movie(
                        title="vidas-pasadas",
                        showtimes=[
                            ShowTime(showtime="18:40", format="2D SUB", seats=168),
                            ShowTime(showtime="21:20", format="2D SUB", seats=169),
                        ],
                    ),
                    Movie(
                        title="anatomía-de-una-caída",
                        showtimes=[
                            ShowTime(showtime="18:50", format="2D SUB", seats=112),
                            ShowTime(showtime="22:10", format="2D SUB", seats=112),
                        ],
                    ),
                ],
            )
        ],
    ),
    ShowDate(
        date="2024-02-06",
        cinemas=[
            Cinema(
                name="cinemark-mallplaza-arica",
                movies=[
                    Movie(title="wonka", showtimes=[]),
                    Movie(title="patos", showtimes=[]),
                    Movie(title="wish", showtimes=[]),
                    Movie(
                        title="los-colonos",
                        showtimes=[
                            ShowTime(showtime="22:20", format="2D SUB", seats=174)
                        ],
                    ),
                    Movie(
                        title="con-todos-menos-contigo",
                        showtimes=[
                            ShowTime(showtime="22:30", format="2D SUB", seats=191)
                        ],
                    ),
                    Movie(
                        title="pobres-criaturas",
                        showtimes=[
                            ShowTime(showtime="11:50", format="2D SUB", seats=263),
                            ShowTime(showtime="15:00", format="2D SUB", seats=263),
                            ShowTime(showtime="18:10", format="2D SUB", seats=263),
                            ShowTime(showtime="21:30", format="2D SUB", seats=261),
                        ],
                    ),
                    Movie(title="masha-y-el-oso", showtimes=[]),
                    Movie(title="el-niño-y-la-garza", showtimes=[]),
                    Movie(
                        title="argylle:-agente-secreto",
                        showtimes=[
                            ShowTime(showtime="22:30", format="2D SUB", seats=170)
                        ],
                    ),
                    Movie(
                        title="chicas-pesadas",
                        showtimes=[
                            ShowTime(showtime="19:10", format="2D SUB", seats=120),
                            ShowTime(showtime="22:00", format="2D SUB", seats=122),
                        ],
                    ),
                    Movie(
                        title="vidas-pasadas",
                        showtimes=[
                            ShowTime(showtime="18:40", format="2D SUB", seats=166),
                            ShowTime(showtime="21:20", format="2D SUB", seats=169),
                        ],
                    ),
                    Movie(
                        title="anatomía-de-una-caída",
                        showtimes=[
                            ShowTime(showtime="18:50", format="2D SUB", seats=110),
                            ShowTime(showtime="22:15", format="2D SUB", seats=112),
                        ],
                    ),
                ],
            )
        ],
    ),
    ShowDate(
        date="2024-02-07",
        cinemas=[
            Cinema(
                name="cinemark-mallplaza-arica",
                movies=[
                    Movie(title="wonka", showtimes=[]),
                    Movie(title="patos", showtimes=[]),
                    Movie(title="wish", showtimes=[]),
                    Movie(
                        title="los-colonos",
                        showtimes=[
                            ShowTime(showtime="22:20", format="2D SUB", seats=174)
                        ],
                    ),
                    Movie(
                        title="con-todos-menos-contigo",
                        showtimes=[
                            ShowTime(showtime="21:50", format="2D SUB", seats=187)
                        ],
                    ),
                    Movie(
                        title="pobres-criaturas",
                        showtimes=[
                            ShowTime(showtime="11:50", format="2D SUB", seats=263),
                            ShowTime(showtime="15:00", format="2D SUB", seats=261),
                            ShowTime(showtime="18:10", format="2D SUB", seats=261),
                            ShowTime(showtime="21:30", format="2D SUB", seats=263),
                        ],
                    ),
                    Movie(title="masha-y-el-oso", showtimes=[]),
                    Movie(
                        title="el-niño-y-la-garza",
                        showtimes=[
                            ShowTime(showtime="19:00", format="2D SUB", seats=191)
                        ],
                    ),
                    Movie(
                        title="argylle:-agente-secreto",
                        showtimes=[
                            ShowTime(showtime="22:30", format="2D SUB", seats=170)
                        ],
                    ),
                    Movie(
                        title="chicas-pesadas",
                        showtimes=[
                            ShowTime(showtime="19:10", format="2D SUB", seats=120),
                            ShowTime(showtime="22:00", format="2D SUB", seats=122),
                        ],
                    ),
                    Movie(
                        title="vidas-pasadas",
                        showtimes=[
                            ShowTime(showtime="18:40", format="2D SUB", seats=169),
                            ShowTime(showtime="21:20", format="2D SUB", seats=169),
                        ],
                    ),
                    Movie(
                        title="anatomía-de-una-caída",
                        showtimes=[
                            ShowTime(showtime="18:50", format="2D SUB", seats=112),
                            ShowTime(showtime="22:10", format="2D SUB", seats=112),
                        ],
                    ),
                ],
            )
        ],
    ),
    ShowDate(
        date="2024-02-22",
        cinemas=[
            Cinema(
                name="cinemark-mallplaza-arica",
                movies=[
                    Movie(
                        title="the-chosen",
                        showtimes=[
                            ShowTime(showtime="20:00", format="2D SUB", seats=100)
                        ],
                    )
                ],
            )
        ],
    ),
    ShowDate(
        date="2024-02-23",
        cinemas=[
            Cinema(
                name="cinemark-mallplaza-arica",
                movies=[
                    Movie(
                        title="the-chosen",
                        showtimes=[
                            ShowTime(showtime="20:00", format="2D SUB", seats=104)
                        ],
                    )
                ],
            )
        ],
    ),
    ShowDate(
        date="2024-02-24",
        cinemas=[
            Cinema(
                name="cinemark-mallplaza-arica",
                movies=[
                    Movie(
                        title="the-chosen",
                        showtimes=[
                            ShowTime(showtime="20:00", format="2D SUB", seats=107)
                        ],
                    )
                ],
            )
        ],
    ),
    ShowDate(
        date="2024-02-25",
        cinemas=[
            Cinema(
                name="cinemark-mallplaza-arica",
                movies=[
                    Movie(
                        title="the-chosen",
                        showtimes=[
                            ShowTime(showtime="20:00", format="2D SUB", seats=112)
                        ],
                    )
                ],
            )
        ],
    ),
    ShowDate(
        date="2024-02-26",
        cinemas=[
            Cinema(
                name="cinemark-mallplaza-arica",
                movies=[
                    Movie(
                        title="the-chosen",
                        showtimes=[
                            ShowTime(showtime="20:00", format="2D SUB", seats=112)
                        ],
                    )
                ],
            )
        ],
    ),
    ShowDate(
        date="2024-02-27",
        cinemas=[
            Cinema(
                name="cinemark-mallplaza-arica",
                movies=[
                    Movie(
                        title="the-chosen",
                        showtimes=[
                            ShowTime(showtime="20:00", format="2D SUB", seats=112)
                        ],
                    )
                ],
            )
        ],
    ),
    ShowDate(
        date="2024-02-28",
        cinemas=[
            Cinema(
                name="cinemark-mallplaza-arica",
                movies=[
                    Movie(
                        title="the-chosen",
                        showtimes=[
                            ShowTime(showtime="20:00", format="2D SUB", seats=112)
                        ],
                    )
                ],
            )
        ],
    ),
]

arica_showdates_fixture = [
    ShowDate(
        date="2024-02-04",
        cinemas=[
            Cinema(
                name="Cinemark MallPlaza Arica",
                movies=[
                    Movie(title="wonka", showtimes=[]),
                    Movie(title="patos", showtimes=[]),
                    Movie(title="wish", showtimes=[]),
                    Movie(
                        title="los-colonos",
                        showtimes=[
                            ShowTime(showtime="22:20", format="2D SUB", seats=174)
                        ],
                    ),
                    Movie(
                        title="con-todos-menos-contigo",
                        showtimes=[
                            ShowTime(showtime="21:50", format="2D SUB", seats=182)
                        ],
                    ),
                    Movie(
                        title="pobres-criaturas",
                        showtimes=[
                            ShowTime(showtime="11:50", format="2D SUB", seats=254),
                            ShowTime(showtime="15:00", format="2D SUB", seats=240),
                            ShowTime(showtime="18:10", format="2D SUB", seats=227),
                            ShowTime(showtime="21:30", format="2D SUB", seats=256),
                        ],
                    ),
                    Movie(title="masha-y-el-oso", showtimes=[]),
                    Movie(
                        title="el-niño-y-la-garza",
                        showtimes=[
                            ShowTime(showtime="19:00", format="2D SUB", seats=170)
                        ],
                    ),
                    Movie(
                        title="argylle:-agente-secreto",
                        showtimes=[
                            ShowTime(showtime="22:30", format="2D SUB", seats=170)
                        ],
                    ),
                    Movie(
                        title="chicas-pesadas",
                        showtimes=[
                            ShowTime(showtime="19:10", format="2D SUB", seats=116),
                            ShowTime(showtime="22:00", format="2D SUB", seats=122),
                        ],
                    ),
                    Movie(
                        title="vidas-pasadas",
                        showtimes=[
                            ShowTime(showtime="18:40", format="2D SUB", seats=148),
                            ShowTime(showtime="21:20", format="2D SUB", seats=167),
                        ],
                    ),
                    Movie(
                        title="anatomía-de-una-caída",
                        showtimes=[
                            ShowTime(showtime="18:50", format="2D SUB", seats=108),
                            ShowTime(showtime="22:10", format="2D SUB", seats=112),
                        ],
                    ),
                ],
            )
        ],
    ),
    ShowDate(
        date="2024-02-05",
        cinemas=[
            Cinema(
                name="Cinemark MallPlaza Arica",
                movies=[
                    Movie(title="wonka", showtimes=[]),
                    Movie(title="patos", showtimes=[]),
                    Movie(title="wish", showtimes=[]),
                    Movie(
                        title="los-colonos",
                        showtimes=[
                            ShowTime(showtime="22:20", format="2D SUB", seats=172)
                        ],
                    ),
                    Movie(
                        title="con-todos-menos-contigo",
                        showtimes=[
                            ShowTime(showtime="21:50", format="2D SUB", seats=191)
                        ],
                    ),
                    Movie(
                        title="pobres-criaturas",
                        showtimes=[
                            ShowTime(showtime="11:50", format="2D SUB", seats=263),
                            ShowTime(showtime="15:00", format="2D SUB", seats=263),
                            ShowTime(showtime="18:10", format="2D SUB", seats=263),
                            ShowTime(showtime="21:30", format="2D SUB", seats=261),
                        ],
                    ),
                    Movie(title="masha-y-el-oso", showtimes=[]),
                    Movie(
                        title="el-niño-y-la-garza",
                        showtimes=[
                            ShowTime(showtime="19:00", format="2D SUB", seats=191)
                        ],
                    ),
                    Movie(
                        title="argylle:-agente-secreto",
                        showtimes=[
                            ShowTime(showtime="22:30", format="2D SUB", seats=170)
                        ],
                    ),
                    Movie(
                        title="chicas-pesadas",
                        showtimes=[
                            ShowTime(showtime="19:10", format="2D SUB", seats=118),
                            ShowTime(showtime="22:00", format="2D SUB", seats=122),
                        ],
                    ),
                    Movie(
                        title="callas-paris-1958",
                        showtimes=[
                            ShowTime(showtime="16:00", format="2D SUB", seats=104)
                        ],
                    ),
                    Movie(
                        title="vidas-pasadas",
                        showtimes=[
                            ShowTime(showtime="18:40", format="2D SUB", seats=168),
                            ShowTime(showtime="21:20", format="2D SUB", seats=169),
                        ],
                    ),
                    Movie(
                        title="anatomía-de-una-caída",
                        showtimes=[
                            ShowTime(showtime="18:50", format="2D SUB", seats=112),
                            ShowTime(showtime="22:10", format="2D SUB", seats=112),
                        ],
                    ),
                ],
            )
        ],
    ),
    ShowDate(
        date="2024-02-06",
        cinemas=[
            Cinema(
                name="Cinemark MallPlaza Arica",
                movies=[
                    Movie(title="wonka", showtimes=[]),
                    Movie(title="patos", showtimes=[]),
                    Movie(title="wish", showtimes=[]),
                    Movie(
                        title="los-colonos",
                        showtimes=[
                            ShowTime(showtime="22:20", format="2D SUB", seats=174)
                        ],
                    ),
                    Movie(
                        title="con-todos-menos-contigo",
                        showtimes=[
                            ShowTime(showtime="22:30", format="2D SUB", seats=191)
                        ],
                    ),
                    Movie(
                        title="pobres-criaturas",
                        showtimes=[
                            ShowTime(showtime="11:50", format="2D SUB", seats=263),
                            ShowTime(showtime="15:00", format="2D SUB", seats=263),
                            ShowTime(showtime="18:10", format="2D SUB", seats=263),
                            ShowTime(showtime="21:30", format="2D SUB", seats=261),
                        ],
                    ),
                    Movie(title="masha-y-el-oso", showtimes=[]),
                    Movie(title="el-niño-y-la-garza", showtimes=[]),
                    Movie(
                        title="argylle:-agente-secreto",
                        showtimes=[
                            ShowTime(showtime="22:30", format="2D SUB", seats=170)
                        ],
                    ),
                    Movie(
                        title="chicas-pesadas",
                        showtimes=[
                            ShowTime(showtime="19:10", format="2D SUB", seats=120),
                            ShowTime(showtime="22:00", format="2D SUB", seats=122),
                        ],
                    ),
                    Movie(
                        title="vidas-pasadas",
                        showtimes=[
                            ShowTime(showtime="18:40", format="2D SUB", seats=166),
                            ShowTime(showtime="21:20", format="2D SUB", seats=169),
                        ],
                    ),
                    Movie(
                        title="anatomía-de-una-caída",
                        showtimes=[
                            ShowTime(showtime="18:50", format="2D SUB", seats=110),
                            ShowTime(showtime="22:15", format="2D SUB", seats=112),
                        ],
                    ),
                ],
            )
        ],
    ),
    ShowDate(
        date="2024-02-07",
        cinemas=[
            Cinema(
                name="Cinemark MallPlaza Arica",
                movies=[
                    Movie(title="wonka", showtimes=[]),
                    Movie(title="patos", showtimes=[]),
                    Movie(title="wish", showtimes=[]),
                    Movie(
                        title="los-colonos",
                        showtimes=[
                            ShowTime(showtime="22:20", format="2D SUB", seats=174)
                        ],
                    ),
                    Movie(
                        title="con-todos-menos-contigo",
                        showtimes=[
                            ShowTime(showtime="21:50", format="2D SUB", seats=187)
                        ],
                    ),
                    Movie(
                        title="pobres-criaturas",
                        showtimes=[
                            ShowTime(showtime="11:50", format="2D SUB", seats=263),
                            ShowTime(showtime="15:00", format="2D SUB", seats=261),
                            ShowTime(showtime="18:10", format="2D SUB", seats=261),
                            ShowTime(showtime="21:30", format="2D SUB", seats=263),
                        ],
                    ),
                    Movie(title="masha-y-el-oso", showtimes=[]),
                    Movie(
                        title="el-niño-y-la-garza",
                        showtimes=[
                            ShowTime(showtime="19:00", format="2D SUB", seats=191)
                        ],
                    ),
                    Movie(
                        title="argylle:-agente-secreto",
                        showtimes=[
                            ShowTime(showtime="22:30", format="2D SUB", seats=170)
                        ],
                    ),
                    Movie(
                        title="chicas-pesadas",
                        showtimes=[
                            ShowTime(showtime="19:10", format="2D SUB", seats=120),
                            ShowTime(showtime="22:00", format="2D SUB", seats=122),
                        ],
                    ),
                    Movie(
                        title="vidas-pasadas",
                        showtimes=[
                            ShowTime(showtime="18:40", format="2D SUB", seats=169),
                            ShowTime(showtime="21:20", format="2D SUB", seats=169),
                        ],
                    ),
                    Movie(
                        title="anatomía-de-una-caída",
                        showtimes=[
                            ShowTime(showtime="18:50", format="2D SUB", seats=112),
                            ShowTime(showtime="22:10", format="2D SUB", seats=112),
                        ],
                    ),
                ],
            )
        ],
    ),
    ShowDate(
        date="2024-02-22",
        cinemas=[
            Cinema(
                name="Cinemark MallPlaza Arica",
                movies=[
                    Movie(
                        title="the-chosen",
                        showtimes=[
                            ShowTime(showtime="20:00", format="2D SUB", seats=100)
                        ],
                    )
                ],
            )
        ],
    ),
    ShowDate(
        date="2024-02-23",
        cinemas=[
            Cinema(
                name="Cinemark MallPlaza Arica",
                movies=[
                    Movie(
                        title="the-chosen",
                        showtimes=[
                            ShowTime(showtime="20:00", format="2D SUB", seats=104)
                        ],
                    )
                ],
            )
        ],
    ),
    ShowDate(
        date="2024-02-24",
        cinemas=[
            Cinema(
                name="Cinemark MallPlaza Arica",
                movies=[
                    Movie(
                        title="the-chosen",
                        showtimes=[
                            ShowTime(showtime="20:00", format="2D SUB", seats=107)
                        ],
                    )
                ],
            )
        ],
    ),
    ShowDate(
        date="2024-02-25",
        cinemas=[
            Cinema(
                name="Cinemark MallPlaza Arica",
                movies=[
                    Movie(
                        title="the-chosen",
                        showtimes=[
                            ShowTime(showtime="20:00", format="2D SUB", seats=112)
                        ],
                    )
                ],
            )
        ],
    ),
    ShowDate(
        date="2024-02-26",
        cinemas=[
            Cinema(
                name="Cinemark MallPlaza Arica",
                movies=[
                    Movie(
                        title="the-chosen",
                        showtimes=[
                            ShowTime(showtime="20:00", format="2D SUB", seats=112)
                        ],
                    )
                ],
            )
        ],
    ),
    ShowDate(
        date="2024-02-27",
        cinemas=[
            Cinema(
                name="Cinemark MallPlaza Arica",
                movies=[
                    Movie(
                        title="the-chosen",
                        showtimes=[
                            ShowTime(showtime="20:00", format="2D SUB", seats=112)
                        ],
                    )
                ],
            )
        ],
    ),
    ShowDate(
        date="2024-02-28",
        cinemas=[
            Cinema(
                name="Cinemark MallPlaza Arica",
                movies=[
                    Movie(
                        title="the-chosen",
                        showtimes=[
                            ShowTime(showtime="20:00", format="2D SUB", seats=112)
                        ],
                    )
                ],
            )
        ],
    ),
]

arica_showdates_february_fixture = ShowDate(
    date="2024-02-04",
    cinemas=[
        Cinema(
            name="Cinemark MallPlaza Arica",
            movies=[
                Movie(title="wonka", showtimes=[]),
                Movie(title="patos", showtimes=[]),
                Movie(title="wish", showtimes=[]),
                Movie(
                    title="los-colonos",
                    showtimes=[ShowTime(showtime="22:20", format="2D SUB", seats=174)],
                ),
                Movie(
                    title="con-todos-menos-contigo",
                    showtimes=[ShowTime(showtime="21:50", format="2D SUB", seats=182)],
                ),
                Movie(
                    title="pobres-criaturas",
                    showtimes=[
                        ShowTime(showtime="11:50", format="2D SUB", seats=254),
                        ShowTime(showtime="15:00", format="2D SUB", seats=240),
                        ShowTime(showtime="18:10", format="2D SUB", seats=227),
                        ShowTime(showtime="21:30", format="2D SUB", seats=256),
                    ],
                ),
                Movie(title="masha-y-el-oso", showtimes=[]),
                Movie(
                    title="el-niño-y-la-garza",
                    showtimes=[ShowTime(showtime="19:00", format="2D SUB", seats=170)],
                ),
                Movie(
                    title="argylle:-agente-secreto",
                    showtimes=[ShowTime(showtime="22:30", format="2D SUB", seats=170)],
                ),
                Movie(
                    title="chicas-pesadas",
                    showtimes=[
                        ShowTime(showtime="19:10", format="2D SUB", seats=116),
                        ShowTime(showtime="22:00", format="2D SUB", seats=122),
                    ],
                ),
                Movie(
                    title="vidas-pasadas",
                    showtimes=[
                        ShowTime(showtime="18:40", format="2D SUB", seats=148),
                        ShowTime(showtime="21:20", format="2D SUB", seats=167),
                    ],
                ),
                Movie(
                    title="anatomía-de-una-caída",
                    showtimes=[
                        ShowTime(showtime="18:50", format="2D SUB", seats=108),
                        ShowTime(showtime="22:10", format="2D SUB", seats=112),
                    ],
                ),
            ],
        )
    ],
)


arica_cinema_showings_fixture = [
    ShowDate(
        date="2024-02-04",
        cinemas=[
            Cinema(
                name="Cinemark MallPlaza Arica",
                movies=[
                    Movie(title="wonka", showtimes=[]),
                    Movie(title="patos", showtimes=[]),
                    Movie(title="wish", showtimes=[]),
                    Movie(
                        title="los-colonos",
                        showtimes=[
                            ShowTime(showtime="22:20", format="2D SUB", seats=174)
                        ],
                    ),
                    Movie(
                        title="con-todos-menos-contigo",
                        showtimes=[
                            ShowTime(showtime="21:50", format="2D SUB", seats=182)
                        ],
                    ),
                    Movie(
                        title="pobres-criaturas",
                        showtimes=[
                            ShowTime(showtime="11:50", format="2D SUB", seats=254),
                            ShowTime(showtime="15:00", format="2D SUB", seats=240),
                            ShowTime(showtime="18:10", format="2D SUB", seats=227),
                            ShowTime(showtime="21:30", format="2D SUB", seats=256),
                        ],
                    ),
                    Movie(title="masha-y-el-oso", showtimes=[]),
                    Movie(
                        title="el-niño-y-la-garza",
                        showtimes=[
                            ShowTime(showtime="19:00", format="2D SUB", seats=170)
                        ],
                    ),
                    Movie(
                        title="argylle:-agente-secreto",
                        showtimes=[
                            ShowTime(showtime="22:30", format="2D SUB", seats=170)
                        ],
                    ),
                    Movie(
                        title="chicas-pesadas",
                        showtimes=[
                            ShowTime(showtime="19:10", format="2D SUB", seats=116),
                            ShowTime(showtime="22:00", format="2D SUB", seats=122),
                        ],
                    ),
                    Movie(
                        title="vidas-pasadas",
                        showtimes=[
                            ShowTime(showtime="18:40", format="2D SUB", seats=148),
                            ShowTime(showtime="21:20", format="2D SUB", seats=167),
                        ],
                    ),
                    Movie(
                        title="anatomía-de-una-caída",
                        showtimes=[
                            ShowTime(showtime="18:50", format="2D SUB", seats=108),
                            ShowTime(showtime="22:10", format="2D SUB", seats=112),
                        ],
                    ),
                ],
            )
        ],
    )
]

arica_total_fixture = [
    Cinema(
        name="Cinemark MallPlaza Arica",
        movies=[
            Movie(title="wonka", showtimes=[]),
            Movie(title="patos", showtimes=[]),
            Movie(title="wish", showtimes=[]),
            Movie(
                title="los-colonos",
                showtimes=[ShowTime(showtime="22:20", format="2D SUB", seats=174)],
            ),
            Movie(
                title="con-todos-menos-contigo",
                showtimes=[ShowTime(showtime="21:50", format="2D SUB", seats=182)],
            ),
            Movie(
                title="pobres-criaturas",
                showtimes=[
                    ShowTime(showtime="11:50", format="2D SUB", seats=254),
                    ShowTime(showtime="15:00", format="2D SUB", seats=240),
                    ShowTime(showtime="18:10", format="2D SUB", seats=227),
                    ShowTime(showtime="21:30", format="2D SUB", seats=256),
                ],
            ),
            Movie(title="masha-y-el-oso", showtimes=[]),
            Movie(
                title="el-niño-y-la-garza",
                showtimes=[ShowTime(showtime="19:00", format="2D SUB", seats=170)],
            ),
            Movie(
                title="argylle:-agente-secreto",
                showtimes=[ShowTime(showtime="22:30", format="2D SUB", seats=170)],
            ),
            Movie(
                title="chicas-pesadas",
                showtimes=[
                    ShowTime(showtime="19:10", format="2D SUB", seats=116),
                    ShowTime(showtime="22:00", format="2D SUB", seats=122),
                ],
            ),
            Movie(
                title="vidas-pasadas",
                showtimes=[
                    ShowTime(showtime="18:40", format="2D SUB", seats=148),
                    ShowTime(showtime="21:20", format="2D SUB", seats=167),
                ],
            ),
            Movie(
                title="anatomía-de-una-caída",
                showtimes=[
                    ShowTime(showtime="18:50", format="2D SUB", seats=108),
                    ShowTime(showtime="22:10", format="2D SUB", seats=112),
                ],
            ),
        ],
    ),
    Cinema(
        name="Cinemark MallPlaza Iquique",
        movies=[
            Movie(title="wonka", showtimes=[]),
            Movie(title="patos", showtimes=[]),
            Movie(title="wish", showtimes=[]),
            Movie(
                title="los-colonos",
                showtimes=[ShowTime(showtime="22:20", format="2D SUB", seats=174)],
            ),
            Movie(
                title="con-todos-menos-contigo",
                showtimes=[ShowTime(showtime="21:50", format="2D SUB", seats=182)],
            ),
            Movie(
                title="pobres-criaturas",
                showtimes=[
                    ShowTime(showtime="11:50", format="2D SUB", seats=254),
                    ShowTime(showtime="15:00", format="2D SUB", seats=240),
                    ShowTime(showtime="18:10", format="2D SUB", seats=227),
                    ShowTime(showtime="21:30", format="2D SUB", seats=256),
                ],
            ),
            Movie(title="masha-y-el-oso", showtimes=[]),
            Movie(
                title="el-niño-y-la-garza",
                showtimes=[ShowTime(showtime="19:00", format="2D SUB", seats=170)],
            ),
            Movie(
                title="argylle:-agente-secreto",
                showtimes=[ShowTime(showtime="22:30", format="2D SUB", seats=170)],
            ),
            Movie(
                title="chicas-pesadas",
                showtimes=[
                    ShowTime(showtime="19:10", format="2D SUB", seats=116),
                    ShowTime(showtime="22:00", format="2D SUB", seats=122),
                ],
            ),
            Movie(
                title="vidas-pasadas",
                showtimes=[
                    ShowTime(showtime="18:40", format="2D SUB", seats=148),
                    ShowTime(showtime="21:20", format="2D SUB", seats=167),
                ],
            ),
            Movie(
                title="anatomía-de-una-caída",
                showtimes=[
                    ShowTime(showtime="18:50", format="2D SUB", seats=108),
                    ShowTime(showtime="22:10", format="2D SUB", seats=112),
                ],
            ),
        ],
    ),
    Cinema(
        name="Cinemark MallPlaza La Serena",
        movies=[
            Movie(title="wonka", showtimes=[]),
            Movie(title="patos", showtimes=[]),
            Movie(title="wish", showtimes=[]),
            Movie(
                title="los-colonos",
                showtimes=[ShowTime(showtime="22:20", format="2D SUB", seats=174)],
            ),
            Movie(
                title="con-todos-menos-contigo",
                showtimes=[ShowTime(showtime="21:50", format="2D SUB", seats=182)],
            ),
            Movie(
                title="pobres-criaturas",
                showtimes=[
                    ShowTime(showtime="11:50", format="2D SUB", seats=254),
                    ShowTime(showtime="15:00", format="2D SUB", seats=240),
                    ShowTime(showtime="18:10", format="2D SUB", seats=227),
                    ShowTime(showtime="21:30", format="2D SUB", seats=256),
                ],
            ),
            Movie(title="masha-y-el-oso", showtimes=[]),
            Movie(
                title="el-niño-y-la-garza",
                showtimes=[ShowTime(showtime="19:00", format="2D SUB", seats=170)],
            ),
            Movie(
                title="argylle:-agente-secreto",
                showtimes=[ShowTime(showtime="22:30", format="2D SUB", seats=170)],
            ),
            Movie(
                title="chicas-pesadas",
                showtimes=[
                    ShowTime(showtime="19:10", format="2D SUB", seats=116),
                    ShowTime(showtime="22:00", format="2D SUB", seats=122),
                ],
            ),
            Movie(
                title="vidas-pasadas",
                showtimes=[
                    ShowTime(showtime="18:40", format="2D SUB", seats=148),
                    ShowTime(showtime="21:20", format="2D SUB", seats=167),
                ],
            ),
            Movie(
                title="anatomía-de-una-caída",
                showtimes=[
                    ShowTime(showtime="18:50", format="2D SUB", seats=108),
                    ShowTime(showtime="22:10", format="2D SUB", seats=112),
                ],
            ),
        ],
    ),
    Cinema(
        name="Cinemark Open Ovalle",
        movies=[
            Movie(title="wonka", showtimes=[]),
            Movie(title="patos", showtimes=[]),
            Movie(title="wish", showtimes=[]),
            Movie(
                title="los-colonos",
                showtimes=[ShowTime(showtime="22:20", format="2D SUB", seats=174)],
            ),
            Movie(
                title="con-todos-menos-contigo",
                showtimes=[ShowTime(showtime="21:50", format="2D SUB", seats=182)],
            ),
            Movie(
                title="pobres-criaturas",
                showtimes=[
                    ShowTime(showtime="11:50", format="2D SUB", seats=254),
                    ShowTime(showtime="15:00", format="2D SUB", seats=240),
                    ShowTime(showtime="18:10", format="2D SUB", seats=227),
                    ShowTime(showtime="21:30", format="2D SUB", seats=256),
                ],
            ),
            Movie(title="masha-y-el-oso", showtimes=[]),
            Movie(
                title="el-niño-y-la-garza",
                showtimes=[ShowTime(showtime="19:00", format="2D SUB", seats=170)],
            ),
            Movie(
                title="argylle:-agente-secreto",
                showtimes=[ShowTime(showtime="22:30", format="2D SUB", seats=170)],
            ),
            Movie(
                title="chicas-pesadas",
                showtimes=[
                    ShowTime(showtime="19:10", format="2D SUB", seats=116),
                    ShowTime(showtime="22:00", format="2D SUB", seats=122),
                ],
            ),
            Movie(
                title="vidas-pasadas",
                showtimes=[
                    ShowTime(showtime="18:40", format="2D SUB", seats=148),
                    ShowTime(showtime="21:20", format="2D SUB", seats=167),
                ],
            ),
            Movie(
                title="anatomía-de-una-caída",
                showtimes=[
                    ShowTime(showtime="18:50", format="2D SUB", seats=108),
                    ShowTime(showtime="22:10", format="2D SUB", seats=112),
                ],
            ),
        ],
    ),
    Cinema(
        name="Cinemark Open La Calera",
        movies=[
            Movie(title="wonka", showtimes=[]),
            Movie(title="patos", showtimes=[]),
            Movie(title="wish", showtimes=[]),
            Movie(
                title="los-colonos",
                showtimes=[ShowTime(showtime="22:20", format="2D SUB", seats=174)],
            ),
            Movie(
                title="con-todos-menos-contigo",
                showtimes=[ShowTime(showtime="21:50", format="2D SUB", seats=182)],
            ),
            Movie(
                title="pobres-criaturas",
                showtimes=[
                    ShowTime(showtime="11:50", format="2D SUB", seats=254),
                    ShowTime(showtime="15:00", format="2D SUB", seats=240),
                    ShowTime(showtime="18:10", format="2D SUB", seats=227),
                    ShowTime(showtime="21:30", format="2D SUB", seats=256),
                ],
            ),
            Movie(title="masha-y-el-oso", showtimes=[]),
            Movie(
                title="el-niño-y-la-garza",
                showtimes=[ShowTime(showtime="19:00", format="2D SUB", seats=170)],
            ),
            Movie(
                title="argylle:-agente-secreto",
                showtimes=[ShowTime(showtime="22:30", format="2D SUB", seats=170)],
            ),
            Movie(
                title="chicas-pesadas",
                showtimes=[
                    ShowTime(showtime="19:10", format="2D SUB", seats=116),
                    ShowTime(showtime="22:00", format="2D SUB", seats=122),
                ],
            ),
            Movie(
                title="vidas-pasadas",
                showtimes=[
                    ShowTime(showtime="18:40", format="2D SUB", seats=148),
                    ShowTime(showtime="21:20", format="2D SUB", seats=167),
                ],
            ),
            Movie(
                title="anatomía-de-una-caída",
                showtimes=[
                    ShowTime(showtime="18:50", format="2D SUB", seats=108),
                    ShowTime(showtime="22:10", format="2D SUB", seats=112),
                ],
            ),
        ],
    ),
    Cinema(
        name="Cinemark Espacio Urbano",
        movies=[
            Movie(title="wonka", showtimes=[]),
            Movie(title="patos", showtimes=[]),
            Movie(title="wish", showtimes=[]),
            Movie(
                title="los-colonos",
                showtimes=[ShowTime(showtime="22:20", format="2D SUB", seats=174)],
            ),
            Movie(
                title="con-todos-menos-contigo",
                showtimes=[ShowTime(showtime="21:50", format="2D SUB", seats=182)],
            ),
            Movie(
                title="pobres-criaturas",
                showtimes=[
                    ShowTime(showtime="11:50", format="2D SUB", seats=254),
                    ShowTime(showtime="15:00", format="2D SUB", seats=240),
                    ShowTime(showtime="18:10", format="2D SUB", seats=227),
                    ShowTime(showtime="21:30", format="2D SUB", seats=256),
                ],
            ),
            Movie(title="masha-y-el-oso", showtimes=[]),
            Movie(
                title="el-niño-y-la-garza",
                showtimes=[ShowTime(showtime="19:00", format="2D SUB", seats=170)],
            ),
            Movie(
                title="argylle:-agente-secreto",
                showtimes=[ShowTime(showtime="22:30", format="2D SUB", seats=170)],
            ),
            Movie(
                title="chicas-pesadas",
                showtimes=[
                    ShowTime(showtime="19:10", format="2D SUB", seats=116),
                    ShowTime(showtime="22:00", format="2D SUB", seats=122),
                ],
            ),
            Movie(
                title="vidas-pasadas",
                showtimes=[
                    ShowTime(showtime="18:40", format="2D SUB", seats=148),
                    ShowTime(showtime="21:20", format="2D SUB", seats=167),
                ],
            ),
            Movie(
                title="anatomía-de-una-caída",
                showtimes=[
                    ShowTime(showtime="18:50", format="2D SUB", seats=108),
                    ShowTime(showtime="22:10", format="2D SUB", seats=112),
                ],
            ),
        ],
    ),
    Cinema(
        name="Cinemark MallMarina",
        movies=[
            Movie(title="wonka", showtimes=[]),
            Movie(title="patos", showtimes=[]),
            Movie(title="wish", showtimes=[]),
            Movie(
                title="los-colonos",
                showtimes=[ShowTime(showtime="22:20", format="2D SUB", seats=174)],
            ),
            Movie(
                title="con-todos-menos-contigo",
                showtimes=[ShowTime(showtime="21:50", format="2D SUB", seats=182)],
            ),
            Movie(
                title="pobres-criaturas",
                showtimes=[
                    ShowTime(showtime="11:50", format="2D SUB", seats=254),
                    ShowTime(showtime="15:00", format="2D SUB", seats=240),
                    ShowTime(showtime="18:10", format="2D SUB", seats=227),
                    ShowTime(showtime="21:30", format="2D SUB", seats=256),
                ],
            ),
            Movie(title="masha-y-el-oso", showtimes=[]),
            Movie(
                title="el-niño-y-la-garza",
                showtimes=[ShowTime(showtime="19:00", format="2D SUB", seats=170)],
            ),
            Movie(
                title="argylle:-agente-secreto",
                showtimes=[ShowTime(showtime="22:30", format="2D SUB", seats=170)],
            ),
            Movie(
                title="chicas-pesadas",
                showtimes=[
                    ShowTime(showtime="19:10", format="2D SUB", seats=116),
                    ShowTime(showtime="22:00", format="2D SUB", seats=122),
                ],
            ),
            Movie(
                title="vidas-pasadas",
                showtimes=[
                    ShowTime(showtime="18:40", format="2D SUB", seats=148),
                    ShowTime(showtime="21:20", format="2D SUB", seats=167),
                ],
            ),
            Movie(
                title="anatomía-de-una-caída",
                showtimes=[
                    ShowTime(showtime="18:50", format="2D SUB", seats=108),
                    ShowTime(showtime="22:10", format="2D SUB", seats=112),
                ],
            ),
        ],
    ),
    Cinema(
        name="Cinemark Alto las Condes",
        movies=[
            Movie(title="wonka", showtimes=[]),
            Movie(title="patos", showtimes=[]),
            Movie(title="wish", showtimes=[]),
            Movie(
                title="los-colonos",
                showtimes=[ShowTime(showtime="22:20", format="2D SUB", seats=174)],
            ),
            Movie(
                title="con-todos-menos-contigo",
                showtimes=[ShowTime(showtime="21:50", format="2D SUB", seats=182)],
            ),
            Movie(
                title="pobres-criaturas",
                showtimes=[
                    ShowTime(showtime="11:50", format="2D SUB", seats=254),
                    ShowTime(showtime="15:00", format="2D SUB", seats=240),
                    ShowTime(showtime="18:10", format="2D SUB", seats=227),
                    ShowTime(showtime="21:30", format="2D SUB", seats=256),
                ],
            ),
            Movie(title="masha-y-el-oso", showtimes=[]),
            Movie(
                title="el-niño-y-la-garza",
                showtimes=[ShowTime(showtime="19:00", format="2D SUB", seats=170)],
            ),
            Movie(
                title="argylle:-agente-secreto",
                showtimes=[ShowTime(showtime="22:30", format="2D SUB", seats=170)],
            ),
            Movie(
                title="chicas-pesadas",
                showtimes=[
                    ShowTime(showtime="19:10", format="2D SUB", seats=116),
                    ShowTime(showtime="22:00", format="2D SUB", seats=122),
                ],
            ),
            Movie(
                title="vidas-pasadas",
                showtimes=[
                    ShowTime(showtime="18:40", format="2D SUB", seats=148),
                    ShowTime(showtime="21:20", format="2D SUB", seats=167),
                ],
            ),
            Movie(
                title="anatomía-de-una-caída",
                showtimes=[
                    ShowTime(showtime="18:50", format="2D SUB", seats=108),
                    ShowTime(showtime="22:10", format="2D SUB", seats=112),
                ],
            ),
        ],
    ),
    Cinema(
        name="Cinemark Portal Ñuñoa",
        movies=[
            Movie(title="wonka", showtimes=[]),
            Movie(title="patos", showtimes=[]),
            Movie(title="wish", showtimes=[]),
            Movie(
                title="los-colonos",
                showtimes=[ShowTime(showtime="22:20", format="2D SUB", seats=174)],
            ),
            Movie(
                title="con-todos-menos-contigo",
                showtimes=[ShowTime(showtime="21:50", format="2D SUB", seats=182)],
            ),
            Movie(
                title="pobres-criaturas",
                showtimes=[
                    ShowTime(showtime="11:50", format="2D SUB", seats=254),
                    ShowTime(showtime="15:00", format="2D SUB", seats=240),
                    ShowTime(showtime="18:10", format="2D SUB", seats=227),
                    ShowTime(showtime="21:30", format="2D SUB", seats=256),
                ],
            ),
            Movie(title="masha-y-el-oso", showtimes=[]),
            Movie(
                title="el-niño-y-la-garza",
                showtimes=[ShowTime(showtime="19:00", format="2D SUB", seats=170)],
            ),
            Movie(
                title="argylle:-agente-secreto",
                showtimes=[ShowTime(showtime="22:30", format="2D SUB", seats=170)],
            ),
            Movie(
                title="chicas-pesadas",
                showtimes=[
                    ShowTime(showtime="19:10", format="2D SUB", seats=116),
                    ShowTime(showtime="22:00", format="2D SUB", seats=122),
                ],
            ),
            Movie(
                title="vidas-pasadas",
                showtimes=[
                    ShowTime(showtime="18:40", format="2D SUB", seats=148),
                    ShowTime(showtime="21:20", format="2D SUB", seats=167),
                ],
            ),
            Movie(
                title="anatomía-de-una-caída",
                showtimes=[
                    ShowTime(showtime="18:50", format="2D SUB", seats=108),
                    ShowTime(showtime="22:10", format="2D SUB", seats=112),
                ],
            ),
        ],
    ),
    Cinema(
        name="Cinemark MallPlaza Norte",
        movies=[
            Movie(title="wonka", showtimes=[]),
            Movie(title="patos", showtimes=[]),
            Movie(title="wish", showtimes=[]),
            Movie(
                title="los-colonos",
                showtimes=[ShowTime(showtime="22:20", format="2D SUB", seats=174)],
            ),
            Movie(
                title="con-todos-menos-contigo",
                showtimes=[ShowTime(showtime="21:50", format="2D SUB", seats=182)],
            ),
            Movie(
                title="pobres-criaturas",
                showtimes=[
                    ShowTime(showtime="11:50", format="2D SUB", seats=254),
                    ShowTime(showtime="15:00", format="2D SUB", seats=240),
                    ShowTime(showtime="18:10", format="2D SUB", seats=227),
                    ShowTime(showtime="21:30", format="2D SUB", seats=256),
                ],
            ),
            Movie(title="masha-y-el-oso", showtimes=[]),
            Movie(
                title="el-niño-y-la-garza",
                showtimes=[ShowTime(showtime="19:00", format="2D SUB", seats=170)],
            ),
            Movie(
                title="argylle:-agente-secreto",
                showtimes=[ShowTime(showtime="22:30", format="2D SUB", seats=170)],
            ),
            Movie(
                title="chicas-pesadas",
                showtimes=[
                    ShowTime(showtime="19:10", format="2D SUB", seats=116),
                    ShowTime(showtime="22:00", format="2D SUB", seats=122),
                ],
            ),
            Movie(
                title="vidas-pasadas",
                showtimes=[
                    ShowTime(showtime="18:40", format="2D SUB", seats=148),
                    ShowTime(showtime="21:20", format="2D SUB", seats=167),
                ],
            ),
            Movie(
                title="anatomía-de-una-caída",
                showtimes=[
                    ShowTime(showtime="18:50", format="2D SUB", seats=108),
                    ShowTime(showtime="22:10", format="2D SUB", seats=112),
                ],
            ),
        ],
    ),
    Cinema(
        name="Cinemark MallPlaza Oeste",
        movies=[
            Movie(title="wonka", showtimes=[]),
            Movie(title="patos", showtimes=[]),
            Movie(title="wish", showtimes=[]),
            Movie(
                title="los-colonos",
                showtimes=[ShowTime(showtime="22:20", format="2D SUB", seats=174)],
            ),
            Movie(
                title="con-todos-menos-contigo",
                showtimes=[ShowTime(showtime="21:50", format="2D SUB", seats=182)],
            ),
            Movie(
                title="pobres-criaturas",
                showtimes=[
                    ShowTime(showtime="11:50", format="2D SUB", seats=254),
                    ShowTime(showtime="15:00", format="2D SUB", seats=240),
                    ShowTime(showtime="18:10", format="2D SUB", seats=227),
                    ShowTime(showtime="21:30", format="2D SUB", seats=256),
                ],
            ),
            Movie(title="masha-y-el-oso", showtimes=[]),
            Movie(
                title="el-niño-y-la-garza",
                showtimes=[ShowTime(showtime="19:00", format="2D SUB", seats=170)],
            ),
            Movie(
                title="argylle:-agente-secreto",
                showtimes=[ShowTime(showtime="22:30", format="2D SUB", seats=170)],
            ),
            Movie(
                title="chicas-pesadas",
                showtimes=[
                    ShowTime(showtime="19:10", format="2D SUB", seats=116),
                    ShowTime(showtime="22:00", format="2D SUB", seats=122),
                ],
            ),
            Movie(
                title="vidas-pasadas",
                showtimes=[
                    ShowTime(showtime="18:40", format="2D SUB", seats=148),
                    ShowTime(showtime="21:20", format="2D SUB", seats=167),
                ],
            ),
            Movie(
                title="anatomía-de-una-caída",
                showtimes=[
                    ShowTime(showtime="18:50", format="2D SUB", seats=108),
                    ShowTime(showtime="22:10", format="2D SUB", seats=112),
                ],
            ),
        ],
    ),
    Cinema(
        name="Cinemark Mid Mall Maipú",
        movies=[
            Movie(title="wonka", showtimes=[]),
            Movie(title="patos", showtimes=[]),
            Movie(title="wish", showtimes=[]),
            Movie(
                title="los-colonos",
                showtimes=[ShowTime(showtime="22:20", format="2D SUB", seats=174)],
            ),
            Movie(
                title="con-todos-menos-contigo",
                showtimes=[ShowTime(showtime="21:50", format="2D SUB", seats=182)],
            ),
            Movie(
                title="pobres-criaturas",
                showtimes=[
                    ShowTime(showtime="11:50", format="2D SUB", seats=254),
                    ShowTime(showtime="15:00", format="2D SUB", seats=240),
                    ShowTime(showtime="18:10", format="2D SUB", seats=227),
                    ShowTime(showtime="21:30", format="2D SUB", seats=256),
                ],
            ),
            Movie(title="masha-y-el-oso", showtimes=[]),
            Movie(
                title="el-niño-y-la-garza",
                showtimes=[ShowTime(showtime="19:00", format="2D SUB", seats=170)],
            ),
            Movie(
                title="argylle:-agente-secreto",
                showtimes=[ShowTime(showtime="22:30", format="2D SUB", seats=170)],
            ),
            Movie(
                title="chicas-pesadas",
                showtimes=[
                    ShowTime(showtime="19:10", format="2D SUB", seats=116),
                    ShowTime(showtime="22:00", format="2D SUB", seats=122),
                ],
            ),
            Movie(
                title="vidas-pasadas",
                showtimes=[
                    ShowTime(showtime="18:40", format="2D SUB", seats=148),
                    ShowTime(showtime="21:20", format="2D SUB", seats=167),
                ],
            ),
            Movie(
                title="anatomía-de-una-caída",
                showtimes=[
                    ShowTime(showtime="18:50", format="2D SUB", seats=108),
                    ShowTime(showtime="22:10", format="2D SUB", seats=112),
                ],
            ),
        ],
    ),
    Cinema(
        name="Cinemark MallPlaza Tobalaba",
        movies=[
            Movie(title="wonka", showtimes=[]),
            Movie(title="patos", showtimes=[]),
            Movie(title="wish", showtimes=[]),
            Movie(
                title="los-colonos",
                showtimes=[ShowTime(showtime="22:20", format="2D SUB", seats=174)],
            ),
            Movie(
                title="con-todos-menos-contigo",
                showtimes=[ShowTime(showtime="21:50", format="2D SUB", seats=182)],
            ),
            Movie(
                title="pobres-criaturas",
                showtimes=[
                    ShowTime(showtime="11:50", format="2D SUB", seats=254),
                    ShowTime(showtime="15:00", format="2D SUB", seats=240),
                    ShowTime(showtime="18:10", format="2D SUB", seats=227),
                    ShowTime(showtime="21:30", format="2D SUB", seats=256),
                ],
            ),
            Movie(title="masha-y-el-oso", showtimes=[]),
            Movie(
                title="el-niño-y-la-garza",
                showtimes=[ShowTime(showtime="19:00", format="2D SUB", seats=170)],
            ),
            Movie(
                title="argylle:-agente-secreto",
                showtimes=[ShowTime(showtime="22:30", format="2D SUB", seats=170)],
            ),
            Movie(
                title="chicas-pesadas",
                showtimes=[
                    ShowTime(showtime="19:10", format="2D SUB", seats=116),
                    ShowTime(showtime="22:00", format="2D SUB", seats=122),
                ],
            ),
            Movie(
                title="vidas-pasadas",
                showtimes=[
                    ShowTime(showtime="18:40", format="2D SUB", seats=148),
                    ShowTime(showtime="21:20", format="2D SUB", seats=167),
                ],
            ),
            Movie(
                title="anatomía-de-una-caída",
                showtimes=[
                    ShowTime(showtime="18:50", format="2D SUB", seats=108),
                    ShowTime(showtime="22:10", format="2D SUB", seats=112),
                ],
            ),
        ],
    ),
    Cinema(
        name="Cinemark MallPlaza Vespucio",
        movies=[
            Movie(title="wonka", showtimes=[]),
            Movie(title="patos", showtimes=[]),
            Movie(title="wish", showtimes=[]),
            Movie(
                title="los-colonos",
                showtimes=[ShowTime(showtime="22:20", format="2D SUB", seats=174)],
            ),
            Movie(
                title="con-todos-menos-contigo",
                showtimes=[ShowTime(showtime="21:50", format="2D SUB", seats=182)],
            ),
            Movie(
                title="pobres-criaturas",
                showtimes=[
                    ShowTime(showtime="11:50", format="2D SUB", seats=254),
                    ShowTime(showtime="15:00", format="2D SUB", seats=240),
                    ShowTime(showtime="18:10", format="2D SUB", seats=227),
                    ShowTime(showtime="21:30", format="2D SUB", seats=256),
                ],
            ),
            Movie(title="masha-y-el-oso", showtimes=[]),
            Movie(
                title="el-niño-y-la-garza",
                showtimes=[ShowTime(showtime="19:00", format="2D SUB", seats=170)],
            ),
            Movie(
                title="argylle:-agente-secreto",
                showtimes=[ShowTime(showtime="22:30", format="2D SUB", seats=170)],
            ),
            Movie(
                title="chicas-pesadas",
                showtimes=[
                    ShowTime(showtime="19:10", format="2D SUB", seats=116),
                    ShowTime(showtime="22:00", format="2D SUB", seats=122),
                ],
            ),
            Movie(
                title="vidas-pasadas",
                showtimes=[
                    ShowTime(showtime="18:40", format="2D SUB", seats=148),
                    ShowTime(showtime="21:20", format="2D SUB", seats=167),
                ],
            ),
            Movie(
                title="anatomía-de-una-caída",
                showtimes=[
                    ShowTime(showtime="18:50", format="2D SUB", seats=108),
                    ShowTime(showtime="22:10", format="2D SUB", seats=112),
                ],
            ),
        ],
    ),
    Cinema(
        name="Cinemark Open Rancagua",
        movies=[
            Movie(title="wonka", showtimes=[]),
            Movie(title="patos", showtimes=[]),
            Movie(title="wish", showtimes=[]),
            Movie(
                title="los-colonos",
                showtimes=[ShowTime(showtime="22:20", format="2D SUB", seats=174)],
            ),
            Movie(
                title="con-todos-menos-contigo",
                showtimes=[ShowTime(showtime="21:50", format="2D SUB", seats=182)],
            ),
            Movie(
                title="pobres-criaturas",
                showtimes=[
                    ShowTime(showtime="11:50", format="2D SUB", seats=254),
                    ShowTime(showtime="15:00", format="2D SUB", seats=240),
                    ShowTime(showtime="18:10", format="2D SUB", seats=227),
                    ShowTime(showtime="21:30", format="2D SUB", seats=256),
                ],
            ),
            Movie(title="masha-y-el-oso", showtimes=[]),
            Movie(
                title="el-niño-y-la-garza",
                showtimes=[ShowTime(showtime="19:00", format="2D SUB", seats=170)],
            ),
            Movie(
                title="argylle:-agente-secreto",
                showtimes=[ShowTime(showtime="22:30", format="2D SUB", seats=170)],
            ),
            Movie(
                title="chicas-pesadas",
                showtimes=[
                    ShowTime(showtime="19:10", format="2D SUB", seats=116),
                    ShowTime(showtime="22:00", format="2D SUB", seats=122),
                ],
            ),
            Movie(
                title="vidas-pasadas",
                showtimes=[
                    ShowTime(showtime="18:40", format="2D SUB", seats=148),
                    ShowTime(showtime="21:20", format="2D SUB", seats=167),
                ],
            ),
            Movie(
                title="anatomía-de-una-caída",
                showtimes=[
                    ShowTime(showtime="18:50", format="2D SUB", seats=108),
                    ShowTime(showtime="22:10", format="2D SUB", seats=112),
                ],
            ),
        ],
    ),
    Cinema(
        name="Cinemark Mall Rancagua",
        movies=[
            Movie(title="wonka", showtimes=[]),
            Movie(title="patos", showtimes=[]),
            Movie(title="wish", showtimes=[]),
            Movie(
                title="los-colonos",
                showtimes=[ShowTime(showtime="22:20", format="2D SUB", seats=174)],
            ),
            Movie(
                title="con-todos-menos-contigo",
                showtimes=[ShowTime(showtime="21:50", format="2D SUB", seats=182)],
            ),
            Movie(
                title="pobres-criaturas",
                showtimes=[
                    ShowTime(showtime="11:50", format="2D SUB", seats=254),
                    ShowTime(showtime="15:00", format="2D SUB", seats=240),
                    ShowTime(showtime="18:10", format="2D SUB", seats=227),
                    ShowTime(showtime="21:30", format="2D SUB", seats=256),
                ],
            ),
            Movie(title="masha-y-el-oso", showtimes=[]),
            Movie(
                title="el-niño-y-la-garza",
                showtimes=[ShowTime(showtime="19:00", format="2D SUB", seats=170)],
            ),
            Movie(
                title="argylle:-agente-secreto",
                showtimes=[ShowTime(showtime="22:30", format="2D SUB", seats=170)],
            ),
            Movie(
                title="chicas-pesadas",
                showtimes=[
                    ShowTime(showtime="19:10", format="2D SUB", seats=116),
                    ShowTime(showtime="22:00", format="2D SUB", seats=122),
                ],
            ),
            Movie(
                title="vidas-pasadas",
                showtimes=[
                    ShowTime(showtime="18:40", format="2D SUB", seats=148),
                    ShowTime(showtime="21:20", format="2D SUB", seats=167),
                ],
            ),
            Movie(
                title="anatomía-de-una-caída",
                showtimes=[
                    ShowTime(showtime="18:50", format="2D SUB", seats=108),
                    ShowTime(showtime="22:10", format="2D SUB", seats=112),
                ],
            ),
        ],
    ),
    Cinema(
        name="Cinemark MallPlaza Trebol",
        movies=[
            Movie(title="wonka", showtimes=[]),
            Movie(title="patos", showtimes=[]),
            Movie(title="wish", showtimes=[]),
            Movie(
                title="los-colonos",
                showtimes=[ShowTime(showtime="22:20", format="2D SUB", seats=174)],
            ),
            Movie(
                title="con-todos-menos-contigo",
                showtimes=[ShowTime(showtime="21:50", format="2D SUB", seats=182)],
            ),
            Movie(
                title="pobres-criaturas",
                showtimes=[
                    ShowTime(showtime="11:50", format="2D SUB", seats=254),
                    ShowTime(showtime="15:00", format="2D SUB", seats=240),
                    ShowTime(showtime="18:10", format="2D SUB", seats=227),
                    ShowTime(showtime="21:30", format="2D SUB", seats=256),
                ],
            ),
            Movie(title="masha-y-el-oso", showtimes=[]),
            Movie(
                title="el-niño-y-la-garza",
                showtimes=[ShowTime(showtime="19:00", format="2D SUB", seats=170)],
            ),
            Movie(
                title="argylle:-agente-secreto",
                showtimes=[ShowTime(showtime="22:30", format="2D SUB", seats=170)],
            ),
            Movie(
                title="chicas-pesadas",
                showtimes=[
                    ShowTime(showtime="19:10", format="2D SUB", seats=116),
                    ShowTime(showtime="22:00", format="2D SUB", seats=122),
                ],
            ),
            Movie(
                title="vidas-pasadas",
                showtimes=[
                    ShowTime(showtime="18:40", format="2D SUB", seats=148),
                    ShowTime(showtime="21:20", format="2D SUB", seats=167),
                ],
            ),
            Movie(
                title="anatomía-de-una-caída",
                showtimes=[
                    ShowTime(showtime="18:50", format="2D SUB", seats=108),
                    ShowTime(showtime="22:10", format="2D SUB", seats=112),
                ],
            ),
        ],
    ),
    Cinema(
        name="Cinemark MallPlaza Mirador Bio-Bio",
        movies=[
            Movie(title="wonka", showtimes=[]),
            Movie(title="patos", showtimes=[]),
            Movie(title="wish", showtimes=[]),
            Movie(
                title="los-colonos",
                showtimes=[ShowTime(showtime="22:20", format="2D SUB", seats=174)],
            ),
            Movie(
                title="con-todos-menos-contigo",
                showtimes=[ShowTime(showtime="21:50", format="2D SUB", seats=182)],
            ),
            Movie(
                title="pobres-criaturas",
                showtimes=[
                    ShowTime(showtime="11:50", format="2D SUB", seats=254),
                    ShowTime(showtime="15:00", format="2D SUB", seats=240),
                    ShowTime(showtime="18:10", format="2D SUB", seats=227),
                    ShowTime(showtime="21:30", format="2D SUB", seats=256),
                ],
            ),
            Movie(title="masha-y-el-oso", showtimes=[]),
            Movie(
                title="el-niño-y-la-garza",
                showtimes=[ShowTime(showtime="19:00", format="2D SUB", seats=170)],
            ),
            Movie(
                title="argylle:-agente-secreto",
                showtimes=[ShowTime(showtime="22:30", format="2D SUB", seats=170)],
            ),
            Movie(
                title="chicas-pesadas",
                showtimes=[
                    ShowTime(showtime="19:10", format="2D SUB", seats=116),
                    ShowTime(showtime="22:00", format="2D SUB", seats=122),
                ],
            ),
            Movie(
                title="vidas-pasadas",
                showtimes=[
                    ShowTime(showtime="18:40", format="2D SUB", seats=148),
                    ShowTime(showtime="21:20", format="2D SUB", seats=167),
                ],
            ),
            Movie(
                title="anatomía-de-una-caída",
                showtimes=[
                    ShowTime(showtime="18:50", format="2D SUB", seats=108),
                    ShowTime(showtime="22:10", format="2D SUB", seats=112),
                ],
            ),
        ],
    ),
    Cinema(
        name="Cinemark Arauco Coronel",
        movies=[
            Movie(title="wonka", showtimes=[]),
            Movie(title="patos", showtimes=[]),
            Movie(title="wish", showtimes=[]),
            Movie(
                title="los-colonos",
                showtimes=[ShowTime(showtime="22:20", format="2D SUB", seats=174)],
            ),
            Movie(
                title="con-todos-menos-contigo",
                showtimes=[ShowTime(showtime="21:50", format="2D SUB", seats=182)],
            ),
            Movie(
                title="pobres-criaturas",
                showtimes=[
                    ShowTime(showtime="11:50", format="2D SUB", seats=254),
                    ShowTime(showtime="15:00", format="2D SUB", seats=240),
                    ShowTime(showtime="18:10", format="2D SUB", seats=227),
                    ShowTime(showtime="21:30", format="2D SUB", seats=256),
                ],
            ),
            Movie(title="masha-y-el-oso", showtimes=[]),
            Movie(
                title="el-niño-y-la-garza",
                showtimes=[ShowTime(showtime="19:00", format="2D SUB", seats=170)],
            ),
            Movie(
                title="argylle:-agente-secreto",
                showtimes=[ShowTime(showtime="22:30", format="2D SUB", seats=170)],
            ),
            Movie(
                title="chicas-pesadas",
                showtimes=[
                    ShowTime(showtime="19:10", format="2D SUB", seats=116),
                    ShowTime(showtime="22:00", format="2D SUB", seats=122),
                ],
            ),
            Movie(
                title="vidas-pasadas",
                showtimes=[
                    ShowTime(showtime="18:40", format="2D SUB", seats=148),
                    ShowTime(showtime="21:20", format="2D SUB", seats=167),
                ],
            ),
            Movie(
                title="anatomía-de-una-caída",
                showtimes=[
                    ShowTime(showtime="18:50", format="2D SUB", seats=108),
                    ShowTime(showtime="22:10", format="2D SUB", seats=112),
                ],
            ),
        ],
    ),
    Cinema(
        name="Cinemark Portal Osorno",
        movies=[
            Movie(title="wonka", showtimes=[]),
            Movie(title="patos", showtimes=[]),
            Movie(title="wish", showtimes=[]),
            Movie(
                title="los-colonos",
                showtimes=[ShowTime(showtime="22:20", format="2D SUB", seats=174)],
            ),
            Movie(
                title="con-todos-menos-contigo",
                showtimes=[ShowTime(showtime="21:50", format="2D SUB", seats=182)],
            ),
            Movie(
                title="pobres-criaturas",
                showtimes=[
                    ShowTime(showtime="11:50", format="2D SUB", seats=254),
                    ShowTime(showtime="15:00", format="2D SUB", seats=240),
                    ShowTime(showtime="18:10", format="2D SUB", seats=227),
                    ShowTime(showtime="21:30", format="2D SUB", seats=256),
                ],
            ),
            Movie(title="masha-y-el-oso", showtimes=[]),
            Movie(
                title="el-niño-y-la-garza",
                showtimes=[ShowTime(showtime="19:00", format="2D SUB", seats=170)],
            ),
            Movie(
                title="argylle:-agente-secreto",
                showtimes=[ShowTime(showtime="22:30", format="2D SUB", seats=170)],
            ),
            Movie(
                title="chicas-pesadas",
                showtimes=[
                    ShowTime(showtime="19:10", format="2D SUB", seats=116),
                    ShowTime(showtime="22:00", format="2D SUB", seats=122),
                ],
            ),
            Movie(
                title="vidas-pasadas",
                showtimes=[
                    ShowTime(showtime="18:40", format="2D SUB", seats=148),
                    ShowTime(showtime="21:20", format="2D SUB", seats=167),
                ],
            ),
            Movie(
                title="anatomía-de-una-caída",
                showtimes=[
                    ShowTime(showtime="18:50", format="2D SUB", seats=108),
                    ShowTime(showtime="22:10", format="2D SUB", seats=112),
                ],
            ),
        ],
    ),
]
