import json

from movie_schedules.dataclasses.cinema import Cinema
from movie_schedules.dataclasses.movie import Movie, ShowTime

with open("tests/fixtures/cinepolis_fixture.json") as f:
    cinepolis_fixture = json.load(f)

showtimes_by_date_fixture = {
    "Movies": [
        {
            "Formats": [
                {
                    "Showtimes": [
                        {
                            "CinemaId": 475,
                            "VistaCinemaId": "730",
                            "ShowtimeId": "51862",
                            "TimeFilter": "/Date(1707066300000)/",
                            "Time": "11:05",
                            "ShowtimeAMPM": "11:05 AM",
                        },
                        {
                            "CinemaId": 475,
                            "VistaCinemaId": "730",
                            "ShowtimeId": "51852",
                            "TimeFilter": "/Date(1707106200000)/",
                            "Time": "22:10",
                            "ShowtimeAMPM": "10:10 PM",
                        },
                    ],
                    "VistaId": "HO00007973",
                    "Name": "ESP",
                    "IsExperience": False,
                    "SegobPermission": None,
                    "Language": "ESPAÑOL",
                }
            ],
            "Id": 44859,
            "Title": "EL NIÑO Y LA GARZA",
            "Key": "el-nino-y-la-garza",
            "OriginalTitle": "EL NIÑO Y LA GARZA",
            "Rating": "TE+7",
            "RatingDescription": "Todo espectador, inconveniente para menores de 7 años: Que contenga imágenes que pueda producir trastornos en el desarrollo de la personalidad infantil y producir confusión entre la realidad y la fantasía.",
            "RunTime": "124 min",
            "Poster": "http://static.cinepolis.com/img/peliculas/44859/1/1/44859.jpg",
            "Trailer": "https://www.youtube.com/watch?v=gl_weMFbo-c",
            "Director": "Hayao Miyazaki",
            "Gender": "",
            "Distributor": "",
            "Order": 0,
            "Actors": [""],
        },
        {
            "Formats": [
                {
                    "Showtimes": [
                        {
                            "CinemaId": 475,
                            "VistaCinemaId": "730",
                            "ShowtimeId": "51863",
                            "TimeFilter": "/Date(1707076200000)/",
                            "Time": "13:50",
                            "ShowtimeAMPM": "01:50 PM",
                        },
                        {
                            "CinemaId": 475,
                            "VistaCinemaId": "730",
                            "ShowtimeId": "51864",
                            "TimeFilter": "/Date(1707085200000)/",
                            "Time": "16:20",
                            "ShowtimeAMPM": "04:20 PM",
                        },
                    ],
                    "VistaId": "HO00007436",
                    "Name": "ESP",
                    "IsExperience": False,
                    "SegobPermission": None,
                    "Language": "ESPAÑOL",
                }
            ],
            "Id": 42468,
            "Title": "WISH: EL PODER DE LOS DESEOS",
            "Key": "wish-el-poder-de-los-deseos",
            "OriginalTitle": "WISH: EL PODER DE LOS DESEOS",
            "Rating": "TE",
            "RatingDescription": "Todo Espectador.",
            "RunTime": "95 min",
            "Poster": "http://static.cinepolis.com/img/peliculas/42468/1/1/42468.jpg",
            "Trailer": "https://www.youtube.com/watch?v=_x5Juvpb7Pk",
            "Director": "Chris  Buck",
            "Gender": "",
            "Distributor": "",
            "Order": 0,
            "Actors": ["Chris  Pine"],
        },
        {
            "Formats": [
                {
                    "Showtimes": [
                        {
                            "CinemaId": 475,
                            "VistaCinemaId": "730",
                            "ShowtimeId": "51865",
                            "TimeFilter": "/Date(1707095400000)/",
                            "Time": "19:10",
                            "ShowtimeAMPM": "07:10 PM",
                        }
                    ],
                    "VistaId": "HO00007894",
                    "Name": "ESP",
                    "IsExperience": False,
                    "SegobPermission": None,
                    "Language": "ESPAÑOL",
                }
            ],
            "Id": 43644,
            "Title": "WONKA",
            "Key": "wonka",
            "OriginalTitle": "WONKA",
            "Rating": "TE",
            "RatingDescription": "Todo Espectador.",
            "RunTime": "117 min",
            "Poster": "http://static.cinepolis.com/img/peliculas/43644/1/1/43644.jpg",
            "Trailer": "https://www.youtube.com/watch?v=eUj6QTAjqEo",
            "Director": "Paul King",
            "Gender": "",
            "Distributor": "",
            "Order": 0,
            "Actors": ["Timothée Chalamet"],
        },
        {
            "Formats": [
                {
                    "Showtimes": [
                        {
                            "CinemaId": 475,
                            "VistaCinemaId": "730",
                            "ShowtimeId": "51857",
                            "TimeFilter": "/Date(1707067800000)/",
                            "Time": "11:30",
                            "ShowtimeAMPM": "11:30 AM",
                        },
                        {
                            "CinemaId": 475,
                            "VistaCinemaId": "730",
                            "ShowtimeId": "51866",
                            "TimeFilter": "/Date(1707105000000)/",
                            "Time": "21:50",
                            "ShowtimeAMPM": "09:50 PM",
                        },
                    ],
                    "VistaId": "HO00007959",
                    "Name": "SUBT",
                    "IsExperience": False,
                    "SegobPermission": None,
                    "Language": "SUBTITULADA",
                }
            ],
            "Id": 44863,
            "Title": "POBRES CRIATURAS",
            "Key": "pobres-criaturas",
            "OriginalTitle": "POBRES CRIATURAS",
            "Rating": "18",
            "RatingDescription": "mayores de 18 años.",
            "RunTime": "141 min",
            "Poster": "http://static.cinepolis.com/img/peliculas/44863/1/1/44863.jpg",
            "Trailer": "https://www.youtube.com/watch?v=xgMzcMab4Vw",
            "Director": "Yorgos Lanthimos",
            "Gender": "",
            "Distributor": "",
            "Order": 0,
            "Actors": ["Mark  Ruffalo"],
        },
        {
            "Formats": [
                {
                    "Showtimes": [
                        {
                            "CinemaId": 475,
                            "VistaCinemaId": "730",
                            "ShowtimeId": "51847",
                            "TimeFilter": "/Date(1707065400000)/",
                            "Time": "10:50",
                            "ShowtimeAMPM": "10:50 AM",
                        }
                    ],
                    "VistaId": "HO00007875",
                    "Name": "ESP",
                    "IsExperience": False,
                    "SegobPermission": None,
                    "Language": "ESPAÑOL",
                }
            ],
            "Id": 44533,
            "Title": "MASHA Y EL OSO: EL DOBLE DE DIVERSION",
            "Key": "masha-y-el-oso-el-doble-de-diversion",
            "OriginalTitle": "MASHA Y EL OSO: EL DOBLE DE DIVERSION",
            "Rating": "TE",
            "RatingDescription": "Todo Espectador.",
            "RunTime": "70 min",
            "Poster": "http://static.cinepolis.com/img/peliculas/44533/1/1/44533.jpg",
            "Trailer": "https://www.youtube.com/watch?v=SZf1U_zvzYw",
            "Director": "",
            "Gender": "",
            "Distributor": "",
            "Order": 0,
            "Actors": [""],
        },
        {
            "Formats": [
                {
                    "Showtimes": [
                        {
                            "CinemaId": 475,
                            "VistaCinemaId": "730",
                            "ShowtimeId": "51848",
                            "TimeFilter": "/Date(1707071700000)/",
                            "Time": "12:35",
                            "ShowtimeAMPM": "12:35 PM",
                        }
                    ],
                    "VistaId": "HO00007821",
                    "Name": "ESP",
                    "IsExperience": False,
                    "SegobPermission": None,
                    "Language": "ESPAÑOL",
                }
            ],
            "Id": 44294,
            "Title": "PATOS",
            "Key": "patos",
            "OriginalTitle": "PATOS",
            "Rating": "TE",
            "RatingDescription": "Todo Espectador.",
            "RunTime": "92 min",
            "Poster": "http://static.cinepolis.com/img/peliculas/44294/1/1/44294.jpg",
            "Trailer": "https://www.youtube.com/watch?v=aQL6cEdnOcc",
            "Director": "Benjamin Renner",
            "Gender": "",
            "Distributor": "",
            "Order": 0,
            "Actors": [" "],
        },
        {
            "Formats": [
                {
                    "Showtimes": [
                        {
                            "CinemaId": 475,
                            "VistaCinemaId": "730",
                            "ShowtimeId": "51849",
                            "TimeFilter": "/Date(1707079500000)/",
                            "Time": "14:45",
                            "ShowtimeAMPM": "02:45 PM",
                        }
                    ],
                    "VistaId": "HO00008039",
                    "Name": "ESP",
                    "IsExperience": False,
                    "SegobPermission": None,
                    "Language": "ESPAÑOL",
                },
                {
                    "Showtimes": [
                        {
                            "CinemaId": 475,
                            "VistaCinemaId": "730",
                            "ShowtimeId": "51851",
                            "TimeFilter": "/Date(1707097200000)/",
                            "Time": "19:40",
                            "ShowtimeAMPM": "07:40 PM",
                        }
                    ],
                    "VistaId": "HO00008038",
                    "Name": "SUBT",
                    "IsExperience": False,
                    "SegobPermission": None,
                    "Language": "SUBTITULADA",
                },
            ],
            "Id": 45193,
            "Title": "CHICAS PESADAS",
            "Key": "chicas-pesadas",
            "OriginalTitle": "CHICAS PESADAS",
            "Rating": "TE+7",
            "RatingDescription": "Todo espectador, inconveniente para menores de 7 años: Que contenga imágenes que pueda producir trastornos en el desarrollo de la personalidad infantil y producir confusión entre la realidad y la fantasía.",
            "RunTime": "112 min",
            "Poster": "http://static.cinepolis.com/img/peliculas/45193/1/1/45193.jpg",
            "Trailer": "",
            "Director": "Samantha  Jayne",
            "Gender": "",
            "Distributor": "",
            "Order": 0,
            "Actors": ["Reneé  Rapp"],
        },
        {
            "Formats": [
                {
                    "Showtimes": [
                        {
                            "CinemaId": 475,
                            "VistaCinemaId": "730",
                            "ShowtimeId": "51850",
                            "TimeFilter": "/Date(1707088500000)/",
                            "Time": "17:15",
                            "ShowtimeAMPM": "05:15 PM",
                        }
                    ],
                    "VistaId": "HO00008014",
                    "Name": "SUBT",
                    "IsExperience": False,
                    "SegobPermission": None,
                    "Language": "SUBTITULADA",
                }
            ],
            "Id": 45085,
            "Title": "VIDAS PASADAS",
            "Key": "vidas-pasadas",
            "OriginalTitle": "VIDAS PASADAS",
            "Rating": "14",
            "RatingDescription": "Mayores de 14 años.",
            "RunTime": "105 min",
            "Poster": "http://static.cinepolis.com/img/peliculas/45085/1/1/45085.jpg",
            "Trailer": "https://www.youtube.com/watch?v=2yVax1un7FQ&t",
            "Director": "Celine Song",
            "Gender": "",
            "Distributor": "",
            "Order": 0,
            "Actors": ["John Magaro"],
        },
        {
            "Formats": [
                {
                    "Showtimes": [
                        {
                            "CinemaId": 475,
                            "VistaCinemaId": "730",
                            "ShowtimeId": "51858",
                            "TimeFilter": "/Date(1707078300000)/",
                            "Time": "14:25",
                            "ShowtimeAMPM": "02:25 PM",
                        }
                    ],
                    "VistaId": "HO00008011",
                    "Name": "ESP",
                    "IsExperience": False,
                    "SegobPermission": None,
                    "Language": "ESPAÑOL",
                },
                {
                    "Showtimes": [
                        {
                            "CinemaId": 475,
                            "VistaCinemaId": "730",
                            "ShowtimeId": "51860",
                            "TimeFilter": "/Date(1707099000000)/",
                            "Time": "20:10",
                            "ShowtimeAMPM": "08:10 PM",
                        },
                        {
                            "CinemaId": 475,
                            "VistaCinemaId": "730",
                            "ShowtimeId": "51956",
                            "TimeFilter": "/Date(1707107400000)/",
                            "Time": "22:30",
                            "ShowtimeAMPM": "10:30 PM",
                        },
                    ],
                    "VistaId": "HO00007960",
                    "Name": "SUBT",
                    "IsExperience": False,
                    "SegobPermission": None,
                    "Language": "SUBTITULADA",
                },
            ],
            "Id": 44860,
            "Title": "CON TODOS MENOS CONTIGO",
            "Key": "con-todos-menos-contigo",
            "OriginalTitle": "CON TODOS MENOS CONTIGO",
            "Rating": "14",
            "RatingDescription": "Mayores de 14 años.",
            "RunTime": "103 min",
            "Poster": "http://static.cinepolis.com/img/peliculas/44860/1/1/44860.jpg",
            "Trailer": "https://www.youtube.com/watch?v=fmSx6eeSR7M",
            "Director": "Will Gluck",
            "Gender": "",
            "Distributor": "",
            "Order": 0,
            "Actors": ["Glen Powell"],
        },
        {
            "Formats": [
                {
                    "Showtimes": [
                        {
                            "CinemaId": 475,
                            "VistaCinemaId": "730",
                            "ShowtimeId": "51859",
                            "TimeFilter": "/Date(1707087300000)/",
                            "Time": "16:55",
                            "ShowtimeAMPM": "04:55 PM",
                        }
                    ],
                    "VistaId": "HO00008015",
                    "Name": "SUBT",
                    "IsExperience": False,
                    "SegobPermission": None,
                    "Language": "SUBTITULADA",
                }
            ],
            "Id": 45084,
            "Title": "ANATOMIA DE UNA CAIDA",
            "Key": "anatomia-de-una-caida",
            "OriginalTitle": "ANATOMIA DE UNA CAIDA",
            "Rating": "14",
            "RatingDescription": "Mayores de 14 años.",
            "RunTime": "151 min",
            "Poster": "http://static.cinepolis.com/img/peliculas/45084/1/1/45084.jpg",
            "Trailer": "https://www.youtube.com/watch?v=Qg_2qB_Q7Pc&t",
            "Director": "Justine Triet",
            "Gender": "",
            "Distributor": "",
            "Order": 0,
            "Actors": ["Milo Machado Graner"],
        },
        {
            "Formats": [
                {
                    "Showtimes": [
                        {
                            "CinemaId": 475,
                            "VistaCinemaId": "730",
                            "ShowtimeId": "51853",
                            "TimeFilter": "/Date(1707070200000)/",
                            "Time": "12:10",
                            "ShowtimeAMPM": "12:10 PM",
                        },
                        {
                            "CinemaId": 475,
                            "VistaCinemaId": "730",
                            "ShowtimeId": "51854",
                            "TimeFilter": "/Date(1707081000000)/",
                            "Time": "15:10",
                            "ShowtimeAMPM": "03:10 PM",
                        },
                        {
                            "CinemaId": 475,
                            "VistaCinemaId": "730",
                            "ShowtimeId": "51855",
                            "TimeFilter": "/Date(1707092100000)/",
                            "Time": "18:15",
                            "ShowtimeAMPM": "06:15 PM",
                        },
                        {
                            "CinemaId": 475,
                            "VistaCinemaId": "730",
                            "ShowtimeId": "51856",
                            "TimeFilter": "/Date(1707102900000)/",
                            "Time": "21:15",
                            "ShowtimeAMPM": "09:15 PM",
                        },
                    ],
                    "VistaId": "HO00008033",
                    "Name": "4DX-2D ESP",
                    "IsExperience": True,
                    "SegobPermission": None,
                    "Language": "ESPAÑOL",
                }
            ],
            "Id": 44864,
            "Title": "ARGYLLE: AGENTE SECRETO",
            "Key": "argylle-agente-secreto",
            "OriginalTitle": "ARGYLLE: AGENTE SECRETO",
            "Rating": "14",
            "RatingDescription": "Mayores de 14 años.",
            "RunTime": "139 min",
            "Poster": "http://static.cinepolis.com/img/peliculas/44864/1/1/44864.jpg",
            "Trailer": "https://www.youtube.com/watch?v=NX_2ZqCWyPk",
            "Director": "Matthew Vaughn",
            "Gender": "",
            "Distributor": "",
            "Order": 0,
            "Actors": ["Sam Rockwell"],
        },
    ],
    "FilterDate": "/Date(1707026400000)/",
    "ShowtimeDate": "04 febrero",
}

sur_de_chile_formatted_showings_fixture = [
    Cinema(
        name="Vivo San Fernando",
        movies=[
            Movie(title="SOBREVIVIENTES DESPUES DEL TERREMOTO", showtimes=[]),
            Movie(title="MASHA Y EL OSO: EL DOBLE DE DIVERSION", showtimes=[]),
            Movie(title="PATOS", showtimes=[]),
            Movie(title="EL NIÑO Y LA GARZA", showtimes=[]),
            Movie(title="WONKA", showtimes=[]),
            Movie(
                title="POBRES CRIATURAS",
                showtimes=[
                    ShowTime(showtime="19:00", format="2D SUB", seats=""),
                    ShowTime(showtime="21:15", format="2D SUB", seats=""),
                ],
            ),
            Movie(title="AQUAMAN Y EL REINO PERDIDO", showtimes=[]),
            Movie(title="CON TODOS MENOS CONTIGO", showtimes=[]),
            Movie(title="WISH: EL PODER DE LOS DESEOS", showtimes=[]),
            Movie(
                title="ARGYLLE: AGENTE SECRETO",
                showtimes=[ShowTime(showtime="20:45", format="2D SUB", seats="")],
            ),
        ],
    ),
    Cinema(
        name="Plaza Maule Talca",
        movies=[
            Movie(title="WISH: EL PODER DE LOS DESEOS", showtimes=[]),
            Movie(title="PATOS", showtimes=[]),
            Movie(
                title="EL NIÑO Y LA GARZA",
                showtimes=[ShowTime(showtime="13:20", format="2D SUB", seats="")],
            ),
            Movie(
                title="CHICAS PESADAS",
                showtimes=[ShowTime(showtime="22:15", format="2D SUB", seats="")],
            ),
            Movie(title="MASHA Y EL OSO: EL DOBLE DE DIVERSION", showtimes=[]),
            Movie(title="AQUAMAN Y EL REINO PERDIDO", showtimes=[]),
            Movie(
                title="CON TODOS MENOS CONTIGO",
                showtimes=[
                    ShowTime(showtime="18:25", format="2D SUB", seats=""),
                    ShowTime(showtime="20:10", format="2D SUB", seats=""),
                    ShowTime(showtime="21:50", format="2D SUB", seats=""),
                ],
            ),
            Movie(title="ARGYLLE: AGENTE SECRETO", showtimes=[]),
            Movie(title="WONKA", showtimes=[]),
            Movie(
                title="ANATOMIA DE UNA CAIDA",
                showtimes=[ShowTime(showtime="21:30", format="2D SUB", seats="")],
            ),
            Movie(
                title="VIDAS PASADAS",
                showtimes=[ShowTime(showtime="17:50", format="2D SUB", seats="")],
            ),
            Movie(title="SLEEP: EL MAL NO DUERME", showtimes=[]),
            Movie(
                title="POBRES CRIATURAS",
                showtimes=[
                    ShowTime(showtime="15:30", format="2D SUB", seats=""),
                    ShowTime(showtime="21:00", format="2D SUB", seats=""),
                ],
            ),
        ],
    ),
    Cinema(
        name="Arauco Chillán",
        movies=[
            Movie(title="EL NIÑO Y LA GARZA", showtimes=[]),
            Movie(title="WISH: EL PODER DE LOS DESEOS", showtimes=[]),
            Movie(title="WONKA", showtimes=[]),
            Movie(
                title="POBRES CRIATURAS",
                showtimes=[
                    ShowTime(showtime="11:30", format="2D SUB", seats=""),
                    ShowTime(showtime="21:50", format="2D SUB", seats=""),
                ],
            ),
            Movie(title="MASHA Y EL OSO: EL DOBLE DE DIVERSION", showtimes=[]),
            Movie(title="PATOS", showtimes=[]),
            Movie(
                title="CHICAS PESADAS",
                showtimes=[ShowTime(showtime="19:40", format="2D SUB", seats="")],
            ),
            Movie(
                title="VIDAS PASADAS",
                showtimes=[ShowTime(showtime="17:15", format="2D SUB", seats="")],
            ),
            Movie(
                title="CON TODOS MENOS CONTIGO",
                showtimes=[
                    ShowTime(showtime="20:10", format="2D SUB", seats=""),
                    ShowTime(showtime="22:30", format="2D SUB", seats=""),
                ],
            ),
            Movie(
                title="ANATOMIA DE UNA CAIDA",
                showtimes=[ShowTime(showtime="16:55", format="2D SUB", seats="")],
            ),
            Movie(title="ARGYLLE: AGENTE SECRETO", showtimes=[]),
        ],
    ),
    Cinema(
        name="Mallplaza Los Ángeles",
        movies=[
            Movie(title="MASHA Y EL OSO: EL DOBLE DE DIVERSION", showtimes=[]),
            Movie(
                title="VIDAS PASADAS",
                showtimes=[
                    ShowTime(showtime="15:20", format="2D SUB", seats=""),
                    ShowTime(showtime="21:30", format="2D SUB", seats=""),
                ],
            ),
            Movie(title="SLEEP: EL MAL NO DUERME", showtimes=[]),
            Movie(
                title="CHICAS PESADAS",
                showtimes=[ShowTime(showtime="22:15", format="2D SUB", seats="")],
            ),
            Movie(title="PATOS", showtimes=[]),
            Movie(
                title="POBRES CRIATURAS",
                showtimes=[
                    ShowTime(showtime="13:10", format="2D SUB", seats=""),
                    ShowTime(showtime="18:00", format="2D SUB", seats=""),
                ],
            ),
            Movie(title="EL NIÑO Y LA GARZA", showtimes=[]),
            Movie(title="AQUAMAN Y EL REINO PERDIDO", showtimes=[]),
            Movie(title="CON TODOS MENOS CONTIGO", showtimes=[]),
            Movie(
                title="ARGYLLE: AGENTE SECRETO",
                showtimes=[ShowTime(showtime="21:00", format="2D SUB", seats="")],
            ),
            Movie(title="WONKA", showtimes=[]),
            Movie(title="WISH: EL PODER DE LOS DESEOS", showtimes=[]),
            Movie(title="JACK EN LA CAJA MALDITA 3: EL ASCENSO", showtimes=[]),
        ],
    ),
    Cinema(
        name="Temuco (Edificio París)",
        movies=[
            Movie(title="WONKA", showtimes=[]),
            Movie(title="CHICAS PESADAS", showtimes=[]),
            Movie(title="WISH: EL PODER DE LOS DESEOS", showtimes=[]),
            Movie(
                title="SLEEP: EL MAL NO DUERME",
                showtimes=[ShowTime(showtime="22:00", format="2D SUB", seats="")],
            ),
            Movie(title="AQUAMAN Y EL REINO PERDIDO", showtimes=[]),
            Movie(title="EL NIÑO Y LA GARZA", showtimes=[]),
            Movie(
                title="ANATOMIA DE UNA CAIDA",
                showtimes=[
                    ShowTime(showtime="16:50", format="2D SUB", seats=""),
                    ShowTime(showtime="20:00", format="2D SUB", seats=""),
                ],
            ),
            Movie(
                title="ARGYLLE: AGENTE SECRETO",
                showtimes=[ShowTime(showtime="21:00", format="2D SUB", seats="")],
            ),
        ],
    ),
    Cinema(
        name="Cinépolis Paseo Costanera Puerto Montt",
        movies=[
            Movie(title="WONKA", showtimes=[]),
            Movie(
                title="VIDAS PASADAS",
                showtimes=[
                    ShowTime(showtime="14:15", format="2D SUB", seats=""),
                    ShowTime(showtime="21:30", format="2D SUB", seats=""),
                ],
            ),
            Movie(
                title="CON TODOS MENOS CONTIGO",
                showtimes=[
                    ShowTime(showtime="15:00", format="2D SUB", seats=""),
                    ShowTime(showtime="21:00", format="2D SUB", seats=""),
                ],
            ),
            Movie(
                title="CHICAS PESADAS",
                showtimes=[ShowTime(showtime="20:45", format="2D SUB", seats="")],
            ),
            Movie(
                title="EL NIÑO Y LA GARZA",
                showtimes=[ShowTime(showtime="20:00", format="2D SUB", seats="")],
            ),
            Movie(
                title="SLEEP: EL MAL NO DUERME",
                showtimes=[ShowTime(showtime="22:15", format="2D SUB", seats="")],
            ),
            Movie(title="AQUAMAN Y EL REINO PERDIDO", showtimes=[]),
            Movie(
                title="ANATOMIA DE UNA CAIDA",
                showtimes=[
                    ShowTime(showtime="13:45", format="2D SUB", seats=""),
                    ShowTime(showtime="21:45", format="SP SUB", seats=""),
                ],
            ),
            Movie(title="ARGYLLE: AGENTE SECRETO", showtimes=[]),
            Movie(
                title="POBRES CRIATURAS",
                showtimes=[
                    ShowTime(showtime="12:45", format="SP SUB", seats=""),
                    ShowTime(showtime="15:45", format="SP SUB", seats=""),
                    ShowTime(showtime="18:45", format="SP SUB", seats=""),
                ],
            ),
            Movie(title="MASHA Y EL OSO: EL DOBLE DE DIVERSION", showtimes=[]),
            Movie(title="WISH: EL PODER DE LOS DESEOS", showtimes=[]),
            Movie(title="JACK EN LA CAJA MALDITA 3: EL ASCENSO", showtimes=[]),
        ],
    ),
    Cinema(
        name="Cinépolis Paseo Chiloé",
        movies=[
            Movie(title="WONKA", showtimes=[]),
            Movie(
                title="POBRES CRIATURAS",
                showtimes=[
                    ShowTime(showtime="19:45", format="2D SUB", seats=""),
                    ShowTime(showtime="21:15", format="2D SUB", seats=""),
                ],
            ),
            Movie(
                title="ARGYLLE: AGENTE SECRETO",
                showtimes=[ShowTime(showtime="21:00", format="2D SUB", seats="")],
            ),
            Movie(title="WISH: EL PODER DE LOS DESEOS", showtimes=[]),
            Movie(
                title="VIDAS PASADAS",
                showtimes=[
                    ShowTime(showtime="15:20", format="2D SUB", seats=""),
                    ShowTime(showtime="20:30", format="2D SUB", seats=""),
                ],
            ),
            Movie(title="AQUAMAN Y EL REINO PERDIDO", showtimes=[]),
            Movie(title="EL NIÑO Y LA GARZA", showtimes=[]),
        ],
    ),
]

sur_chile_total_fixture = [
    Cinema(
        name="Vivo San Fernando",
        movies=[
            Movie(
                title="SOBREVIVIENTES DESPUES DEL TERREMOTO",
                showtimes=[
                    ShowTime(showtime="11:15", format="2D ESP", seats=""),
                    ShowTime(showtime="22:00", format="2D ESP", seats=""),
                ],
            ),
            Movie(
                title="MASHA Y EL OSO: EL DOBLE DE DIVERSION",
                showtimes=[ShowTime(showtime="14:00", format="2D ESP", seats="")],
            ),
            Movie(
                title="PATOS",
                showtimes=[
                    ShowTime(showtime="11:00", format="2D ESP", seats=""),
                    ShowTime(showtime="16:00", format="2D ESP", seats=""),
                ],
            ),
            Movie(
                title="EL NIÑO Y LA GARZA",
                showtimes=[
                    ShowTime(showtime="18:15", format="2D ESP", seats=""),
                    ShowTime(showtime="21:00", format="2D ESP", seats=""),
                ],
            ),
            Movie(
                title="WONKA",
                showtimes=[
                    ShowTime(showtime="13:00", format="2D ESP", seats=""),
                    ShowTime(showtime="15:45", format="2D ESP", seats=""),
                    ShowTime(showtime="18:45", format="2D ESP", seats=""),
                ],
            ),
            Movie(title="POBRES CRIATURAS", showtimes=[]),
            Movie(
                title="AQUAMAN Y EL REINO PERDIDO",
                showtimes=[
                    ShowTime(showtime="12:30", format="2D ESP", seats=""),
                    ShowTime(showtime="15:15", format="2D ESP", seats=""),
                ],
            ),
            Movie(
                title="CON TODOS MENOS CONTIGO",
                showtimes=[
                    ShowTime(showtime="17:50", format="2D ESP", seats=""),
                    ShowTime(showtime="20:20", format="2D ESP", seats=""),
                ],
            ),
            Movie(
                title="WISH: EL PODER DE LOS DESEOS",
                showtimes=[
                    ShowTime(showtime="12:00", format="2D ESP", seats=""),
                    ShowTime(showtime="14:15", format="2D ESP", seats=""),
                    ShowTime(showtime="16:45", format="2D ESP", seats=""),
                ],
            ),
            Movie(
                title="ARGYLLE: AGENTE SECRETO",
                showtimes=[
                    ShowTime(showtime="11:30", format="2D ESP", seats=""),
                    ShowTime(showtime="14:30", format="2D ESP", seats=""),
                    ShowTime(showtime="17:30", format="2D ESP", seats=""),
                ],
            ),
        ],
    ),
    Cinema(
        name="Plaza Maule Talca",
        movies=[
            Movie(
                title="WISH: EL PODER DE LOS DESEOS",
                showtimes=[
                    ShowTime(showtime="10:30", format="2D ESP", seats=""),
                    ShowTime(showtime="15:00", format="2D ESP", seats=""),
                    ShowTime(showtime="17:10", format="2D ESP", seats=""),
                ],
            ),
            Movie(
                title="PATOS",
                showtimes=[ShowTime(showtime="12:40", format="2D ESP", seats="")],
            ),
            Movie(
                title="EL NIÑO Y LA GARZA",
                showtimes=[ShowTime(showtime="19:35", format="2D ESP", seats="")],
            ),
            Movie(
                title="CHICAS PESADAS",
                showtimes=[
                    ShowTime(showtime="11:55", format="2D ESP", seats=""),
                    ShowTime(showtime="19:05", format="2D ESP", seats=""),
                ],
            ),
            Movie(
                title="MASHA Y EL OSO: EL DOBLE DE DIVERSION",
                showtimes=[ShowTime(showtime="11:30", format="2D ESP", seats="")],
            ),
            Movie(
                title="AQUAMAN Y EL REINO PERDIDO",
                showtimes=[
                    ShowTime(showtime="14:40", format="2D ESP", seats=""),
                    ShowTime(showtime="16:00", format="2D ESP", seats=""),
                ],
            ),
            Movie(
                title="CON TODOS MENOS CONTIGO",
                showtimes=[
                    ShowTime(showtime="10:40", format="2D ESP", seats=""),
                    ShowTime(showtime="19:15", format="2D ESP", seats=""),
                ],
            ),
            Movie(
                title="ARGYLLE: AGENTE SECRETO",
                showtimes=[
                    ShowTime(showtime="11:10", format="4DX-2D ESP", seats=""),
                    ShowTime(showtime="14:10", format="4DX-2D ESP", seats=""),
                    ShowTime(showtime="17:30", format="4DX-2D ESP", seats=""),
                    ShowTime(showtime="20:30", format="4DX-2D ESP", seats=""),
                ],
            ),
            Movie(
                title="WONKA",
                showtimes=[
                    ShowTime(showtime="10:55", format="2D ESP", seats=""),
                    ShowTime(showtime="13:40", format="2D ESP", seats=""),
                    ShowTime(showtime="16:20", format="2D ESP", seats=""),
                ],
            ),
            Movie(title="ANATOMIA DE UNA CAIDA", showtimes=[]),
            Movie(title="VIDAS PASADAS", showtimes=[]),
            Movie(
                title="SLEEP: EL MAL NO DUERME",
                showtimes=[
                    ShowTime(showtime="13:00", format="2D ESP", seats=""),
                    ShowTime(showtime="22:30", format="2D ESP", seats=""),
                ],
            ),
            Movie(title="POBRES CRIATURAS", showtimes=[]),
        ],
    ),
    Cinema(
        name="Arauco Chillán",
        movies=[
            Movie(
                title="EL NIÑO Y LA GARZA",
                showtimes=[
                    ShowTime(showtime="11:05", format="2D ESP", seats=""),
                    ShowTime(showtime="22:10", format="2D ESP", seats=""),
                ],
            ),
            Movie(
                title="WISH: EL PODER DE LOS DESEOS",
                showtimes=[
                    ShowTime(showtime="13:50", format="2D ESP", seats=""),
                    ShowTime(showtime="16:20", format="2D ESP", seats=""),
                ],
            ),
            Movie(
                title="WONKA",
                showtimes=[ShowTime(showtime="19:10", format="2D ESP", seats="")],
            ),
            Movie(title="POBRES CRIATURAS", showtimes=[]),
            Movie(
                title="MASHA Y EL OSO: EL DOBLE DE DIVERSION",
                showtimes=[ShowTime(showtime="10:50", format="2D ESP", seats="")],
            ),
            Movie(
                title="PATOS",
                showtimes=[ShowTime(showtime="12:35", format="2D ESP", seats="")],
            ),
            Movie(
                title="CHICAS PESADAS",
                showtimes=[ShowTime(showtime="14:45", format="2D ESP", seats="")],
            ),
            Movie(title="VIDAS PASADAS", showtimes=[]),
            Movie(
                title="CON TODOS MENOS CONTIGO",
                showtimes=[ShowTime(showtime="14:25", format="2D ESP", seats="")],
            ),
            Movie(title="ANATOMIA DE UNA CAIDA", showtimes=[]),
            Movie(
                title="ARGYLLE: AGENTE SECRETO",
                showtimes=[
                    ShowTime(showtime="12:10", format="4DX-2D ESP", seats=""),
                    ShowTime(showtime="15:10", format="4DX-2D ESP", seats=""),
                    ShowTime(showtime="18:15", format="4DX-2D ESP", seats=""),
                    ShowTime(showtime="21:15", format="4DX-2D ESP", seats=""),
                ],
            ),
        ],
    ),
    Cinema(
        name="Mallplaza Los Ángeles",
        movies=[
            Movie(
                title="MASHA Y EL OSO: EL DOBLE DE DIVERSION",
                showtimes=[
                    ShowTime(showtime="11:40", format="2D ESP", seats=""),
                    ShowTime(showtime="13:25", format="2D ESP", seats=""),
                ],
            ),
            Movie(title="VIDAS PASADAS", showtimes=[]),
            Movie(
                title="SLEEP: EL MAL NO DUERME",
                showtimes=[
                    ShowTime(showtime="17:40", format="2D ESP", seats=""),
                    ShowTime(showtime="21:45", format="2D ESP", seats=""),
                ],
            ),
            Movie(
                title="CHICAS PESADAS",
                showtimes=[ShowTime(showtime="19:50", format="2D ESP", seats="")],
            ),
            Movie(
                title="PATOS",
                showtimes=[
                    ShowTime(showtime="11:00", format="2D ESP", seats=""),
                    ShowTime(showtime="13:40", format="2D ESP", seats=""),
                ],
            ),
            Movie(title="POBRES CRIATURAS", showtimes=[]),
            Movie(
                title="EL NIÑO Y LA GARZA",
                showtimes=[
                    ShowTime(showtime="16:10", format="2D ESP", seats=""),
                    ShowTime(showtime="18:50", format="2D ESP", seats=""),
                ],
            ),
            Movie(
                title="AQUAMAN Y EL REINO PERDIDO",
                showtimes=[
                    ShowTime(showtime="11:10", format="2D ESP", seats=""),
                    ShowTime(showtime="15:50", format="2D ESP", seats=""),
                ],
            ),
            Movie(
                title="CON TODOS MENOS CONTIGO",
                showtimes=[
                    ShowTime(showtime="12:00", format="2D ESP", seats=""),
                    ShowTime(showtime="18:25", format="2D ESP", seats=""),
                    ShowTime(showtime="19:30", format="2D ESP", seats=""),
                    ShowTime(showtime="21:15", format="2D ESP", seats=""),
                ],
            ),
            Movie(
                title="ARGYLLE: AGENTE SECRETO",
                showtimes=[ShowTime(showtime="15:00", format="2D ESP", seats="")],
            ),
            Movie(
                title="WONKA",
                showtimes=[
                    ShowTime(showtime="11:30", format="2D ESP", seats=""),
                    ShowTime(showtime="14:00", format="2D ESP", seats=""),
                    ShowTime(showtime="16:35", format="2D ESP", seats=""),
                    ShowTime(showtime="19:10", format="2D ESP", seats=""),
                ],
            ),
            Movie(
                title="WISH: EL PODER DE LOS DESEOS",
                showtimes=[
                    ShowTime(showtime="12:30", format="2D ESP", seats=""),
                    ShowTime(showtime="14:40", format="2D ESP", seats=""),
                    ShowTime(showtime="17:05", format="2D ESP", seats=""),
                ],
            ),
            Movie(
                title="JACK EN LA CAJA MALDITA 3: EL ASCENSO",
                showtimes=[ShowTime(showtime="22:00", format="2D ESP", seats="")],
            ),
        ],
    ),
    Cinema(
        name="Temuco (Edificio París)",
        movies=[
            Movie(
                title="WONKA",
                showtimes=[
                    ShowTime(showtime="13:00", format="2D ESP", seats=""),
                    ShowTime(showtime="18:10", format="2D ESP", seats=""),
                ],
            ),
            Movie(
                title="CHICAS PESADAS",
                showtimes=[
                    ShowTime(showtime="15:40", format="2D ESP", seats=""),
                    ShowTime(showtime="20:45", format="2D ESP", seats=""),
                ],
            ),
            Movie(
                title="WISH: EL PODER DE LOS DESEOS",
                showtimes=[
                    ShowTime(showtime="12:40", format="2D ESP", seats=""),
                    ShowTime(showtime="15:00", format="2D ESP", seats=""),
                    ShowTime(showtime="17:20", format="2D ESP", seats=""),
                ],
            ),
            Movie(
                title="SLEEP: EL MAL NO DUERME",
                showtimes=[ShowTime(showtime="19:45", format="2D ESP", seats="")],
            ),
            Movie(
                title="AQUAMAN Y EL REINO PERDIDO",
                showtimes=[
                    ShowTime(showtime="11:30", format="2D ESP", seats=""),
                    ShowTime(showtime="16:00", format="2D ESP", seats=""),
                    ShowTime(showtime="21:30", format="2D ESP", seats=""),
                ],
            ),
            Movie(
                title="EL NIÑO Y LA GARZA",
                showtimes=[
                    ShowTime(showtime="13:15", format="2D ESP", seats=""),
                    ShowTime(showtime="14:05", format="2D ESP", seats=""),
                    ShowTime(showtime="18:40", format="2D ESP", seats=""),
                ],
            ),
            Movie(title="ANATOMIA DE UNA CAIDA", showtimes=[]),
            Movie(
                title="ARGYLLE: AGENTE SECRETO",
                showtimes=[
                    ShowTime(showtime="11:45", format="2D ESP", seats=""),
                    ShowTime(showtime="14:45", format="2D ESP", seats=""),
                    ShowTime(showtime="17:50", format="2D ESP", seats=""),
                ],
            ),
        ],
    ),
    Cinema(
        name="Cinépolis Paseo Costanera Puerto Montt",
        movies=[
            Movie(
                title="WONKA",
                showtimes=[
                    ShowTime(showtime="13:30", format="2D ESP", seats=""),
                    ShowTime(showtime="16:15", format="2D ESP", seats=""),
                    ShowTime(showtime="19:00", format="2D ESP", seats=""),
                ],
            ),
            Movie(title="VIDAS PASADAS", showtimes=[]),
            Movie(
                title="CON TODOS MENOS CONTIGO",
                showtimes=[
                    ShowTime(showtime="12:30", format="2D ESP", seats=""),
                    ShowTime(showtime="16:00", format="2D ESP", seats=""),
                    ShowTime(showtime="18:30", format="2D ESP", seats=""),
                    ShowTime(showtime="22:00", format="2D ESP", seats=""),
                ],
            ),
            Movie(
                title="CHICAS PESADAS",
                showtimes=[ShowTime(showtime="18:00", format="2D ESP", seats="")],
            ),
            Movie(
                title="EL NIÑO Y LA GARZA",
                showtimes=[
                    ShowTime(showtime="11:20", format="2D ESP", seats=""),
                    ShowTime(showtime="19:15", format="2D ESP", seats=""),
                ],
            ),
            Movie(
                title="SLEEP: EL MAL NO DUERME",
                showtimes=[ShowTime(showtime="17:00", format="2D ESP", seats="")],
            ),
            Movie(
                title="AQUAMAN Y EL REINO PERDIDO",
                showtimes=[
                    ShowTime(showtime="11:10", format="2D ESP", seats=""),
                    ShowTime(showtime="17:10", format="2D ESP", seats=""),
                    ShowTime(showtime="19:45", format="2D ESP", seats=""),
                ],
            ),
            Movie(title="ANATOMIA DE UNA CAIDA", showtimes=[]),
            Movie(
                title="ARGYLLE: AGENTE SECRETO",
                showtimes=[
                    ShowTime(showtime="11:30", format="2D ESP", seats=""),
                    ShowTime(showtime="14:30", format="2D ESP", seats=""),
                    ShowTime(showtime="17:30", format="2D ESP", seats=""),
                    ShowTime(showtime="20:30", format="2D ESP", seats=""),
                ],
            ),
            Movie(title="POBRES CRIATURAS", showtimes=[]),
            Movie(
                title="MASHA Y EL OSO: EL DOBLE DE DIVERSION",
                showtimes=[
                    ShowTime(showtime="12:15", format="2D ESP", seats=""),
                    ShowTime(showtime="14:00", format="2D ESP", seats=""),
                ],
            ),
            Movie(
                title="WISH: EL PODER DE LOS DESEOS",
                showtimes=[
                    ShowTime(showtime="11:00", format="2D ESP", seats=""),
                    ShowTime(showtime="13:15", format="2D ESP", seats=""),
                    ShowTime(showtime="15:30", format="2D ESP", seats=""),
                    ShowTime(showtime="17:45", format="2D ESP", seats=""),
                ],
            ),
            Movie(
                title="JACK EN LA CAJA MALDITA 3: EL ASCENSO",
                showtimes=[ShowTime(showtime="22:35", format="2D ESP", seats="")],
            ),
        ],
    ),
    Cinema(
        name="Cinépolis Paseo Chiloé",
        movies=[
            Movie(
                title="WONKA",
                showtimes=[
                    ShowTime(showtime="14:20", format="2D ESP", seats=""),
                    ShowTime(showtime="17:00", format="2D ESP", seats=""),
                ],
            ),
            Movie(title="POBRES CRIATURAS", showtimes=[]),
            Movie(
                title="ARGYLLE: AGENTE SECRETO",
                showtimes=[
                    ShowTime(showtime="12:00", format="2D ESP", seats=""),
                    ShowTime(showtime="15:00", format="2D ESP", seats=""),
                    ShowTime(showtime="18:00", format="2D ESP", seats=""),
                ],
            ),
            Movie(
                title="WISH: EL PODER DE LOS DESEOS",
                showtimes=[
                    ShowTime(showtime="12:45", format="2D ESP", seats=""),
                    ShowTime(showtime="14:00", format="2D ESP", seats=""),
                    ShowTime(showtime="16:15", format="2D ESP", seats=""),
                ],
            ),
            Movie(title="VIDAS PASADAS", showtimes=[]),
            Movie(
                title="AQUAMAN Y EL REINO PERDIDO",
                showtimes=[ShowTime(showtime="17:45", format="2D ESP", seats="")],
            ),
            Movie(
                title="EL NIÑO Y LA GARZA",
                showtimes=[ShowTime(showtime="18:30", format="2D ESP", seats="")],
            ),
        ],
    ),
]
