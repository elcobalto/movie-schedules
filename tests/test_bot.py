import unittest
from datetime import datetime
from unittest.mock import patch

from movie_schedules.dataclasses.cinema import Cinema, ShowDate
from movie_schedules.dataclasses.movie import Movie, ShowTime
from movie_schedules.services.bot import CinemaBot
from tests.fixtures.cinemark_expected_results import (
    arica_cinema_showings_fixture,
    arica_showdates_february_fixture,
    arica_showdates_fixture,
    arica_total_fixture,
    arica_wonka_showings_fixture,
    cinemark_fixture,
    mallplaza_airca_wonka_showings_fixture,
    mallplaza_arica_movie_showtimes,
    mallplaza_arica_showdates_fixture,
    wonka_february_showings_fixture,
)
from tests.fixtures.cinepolis_expected_results import (
    cinepolis_fixture,
    showtimes_by_date_fixture,
    sur_chile_total_fixture,
)


class TestCinemaBot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cinema_bot = CinemaBot()

    # Mock data for testing
    cinepolis_showings = [
        Cinema(
            name="Cinepolis",
            movies=[
                Movie(
                    title="Movie1",
                    showtimes=[
                        ShowTime(showtime="14:00", format="2D ESP", seats="100")
                    ],
                )
            ],
        ),
    ]
    cinemark_showings = [
        Cinema(
            name="Cinemark",
            movies=[
                Movie(
                    title="Movie2",
                    showtimes=[ShowTime(showtime="16:30", format="3D", seats="50")],
                )
            ],
        ),
    ]

    @patch("movie_schedules.services.cinemark.CinemarkService.is_chain")
    @patch("movie_schedules.services.cinepolis.CinepolisService.is_chain")
    def test_get_chain_cinepolis(self, mock_cinepolis_is_chain, mock_cinemark_is_chain):
        mock_cinepolis_is_chain.return_value = True
        mock_cinemark_is_chain.return_value = False

        chain = self.cinema_bot.get_chain("cinepolis_cinema")

        self.assertEqual(chain, "CINEHOYTS")

    @patch("movie_schedules.services.cinemark.CinemarkService.is_chain")
    @patch("movie_schedules.services.cinepolis.CinepolisService.is_chain")
    def test_get_chain_cinemark(self, mock_cinepolis_is_chain, mock_cinemark_is_chain):
        mock_cinepolis_is_chain.return_value = False
        mock_cinemark_is_chain.return_value = True

        chain = self.cinema_bot.get_chain("cinemark_cinema")

        self.assertEqual(chain, "CINEMARK")

    @patch("movie_schedules.services.cinepolis.CinepolisService.get_showings")
    def test_get_showings_cinepolis(self, mock_cinepolis_get_showings):
        mock_cinepolis_get_showings.return_value = self.cinepolis_showings

        result = self.cinema_bot.get_showings(
            "wonka", "2-febrero", "cinepolis-la-reina", "ESP"
        )

        self.assertEqual(
            result,
            [
                Cinema(
                    name="Cinepolis",
                    movies=[
                        Movie(
                            title="Movie1",
                            showtimes=[
                                ShowTime(showtime="14:00", format="2D ESP", seats="100")
                            ],
                        )
                    ],
                )
            ],
        )

    @patch("movie_schedules.services.cinemark.CinemarkService.get_showings")
    def test_get_showings_cinemark(self, mock_cinemark_get_showings):
        mock_cinemark_get_showings.return_value = self.cinemark_showings

        result = self.cinema_bot.get_showings(
            "wonka", "4-febrero", "portal-nunoa", "ESP"
        )

        print(result)
        self.assertEqual(
            result,
            [
                Cinema(
                    name="Cinemark",
                    movies=[
                        Movie(
                            title="Movie2",
                            showtimes=[
                                ShowTime(showtime="16:30", format="3D", seats="50")
                            ],
                        )
                    ],
                )
            ],
        )

    @patch("movie_schedules.services.cinemark.CinemarkService.get_showings_by_zone")
    @patch("movie_schedules.services.cinepolis.CinepolisService.get_showings_by_zone")
    def test_get_showings_by_zone(
        self, mock_cinepolis_get_showings, mock_cinemark_get_showings
    ):
        mock_cinepolis_get_showings.return_value = self.cinepolis_showings
        mock_cinemark_get_showings.return_value = self.cinemark_showings

        result = self.cinema_bot.get_showings_by_zone(
            "wonka", "2-febrero", "portal-nunoa", "ESP"
        )

        expected_showings = ShowDate(
            date="2-febrero",
            cinemas=[
                Cinema(
                    name="Cinepolis",
                    movies=[
                        Movie(
                            title="Movie1",
                            showtimes=[
                                ShowTime(showtime="14:00", format="2D ESP", seats="100")
                            ],
                        )
                    ],
                ),
                Cinema(
                    name="Cinemark",
                    movies=[
                        Movie(
                            title="Movie2",
                            showtimes=[
                                ShowTime(showtime="16:30", format="3D", seats="50")
                            ],
                        )
                    ],
                ),
            ],
        )

        self.assertEqual(result, expected_showings)

    @patch("movie_schedules.services.cinemark.CinemarkService.get_showing_by_date")
    @patch("movie_schedules.services.cinepolis.CinepolisService.get_showing_by_date")
    def test_get_showing_by_date(
        self, mock_cinepolis_get_showing, mock_cinemark_get_showing
    ):
        mock_cinepolis_get_showing.return_value = self.cinepolis_showings
        mock_cinemark_get_showing.return_value = self.cinemark_showings

        result = self.cinema_bot.get_showing_by_date("wonka", "2-febrero", "SUB")

        expected_showings = ShowDate(
            date="2-febrero",
            cinemas=[
                Cinema(
                    name="Cinepolis",
                    movies=[
                        Movie(
                            title="Movie1",
                            showtimes=[
                                ShowTime(showtime="14:00", format="2D ESP", seats="100")
                            ],
                        )
                    ],
                ),
                Cinema(
                    name="Cinemark",
                    movies=[
                        Movie(
                            title="Movie2",
                            showtimes=[
                                ShowTime(showtime="16:30", format="3D", seats="50")
                            ],
                        )
                    ],
                ),
            ],
        )

        self.assertEqual(result, expected_showings)

    """
    @patch("movie_schedules.services.cinemark.CinemarkService.get_general_showings")
    @patch("movie_schedules.services.cinepolis.CinepolisService.get_general_showings")
    def test_get_general_showings(self, mock_cinepolis_general_showings, mock_cinemark_general_showings):
        mock_cinepolis_general_showings.return_value = ("Message", 10)
        mock_cinemark_general_showings.return_value = ("Message", 5)

        message, total = self.cinema_bot.get_general_showings("Movie", "2024-02-05", "Cinema", "Format")

        expected_message = "Message"
        expected_total = 15

        self.assertEqual(message, expected_message)
        self.assertEqual(total, expected_total)
    """

    @patch("movie_schedules.services.cinemark.CinemarkService.get_showing_by_cinema")
    @patch("movie_schedules.services.cinepolis.CinepolisService.get_showing_by_cinema")
    def test_get_showing_by_cinema(
        self, mock_cinepolis_get_showing, mock_cinemark_get_showing
    ):
        mock_cinepolis_get_showing.return_value = [
            ShowDate(date=datetime(2024, 2, 5), cinemas=self.cinepolis_showings)
        ]
        mock_cinemark_get_showing.return_value = [
            ShowDate(date=datetime(2024, 2, 5), cinemas=self.cinemark_showings)
        ]

        result = self.cinema_bot.get_showing_by_cinema("Movie", "Cinema", "Format")

        expected_showings = [
            ShowDate(date=datetime(2024, 2, 5), cinemas=self.cinepolis_showings),
            ShowDate(date=datetime(2024, 2, 5), cinemas=self.cinemark_showings),
        ]

        self.assertEqual(result, expected_showings)

    @patch(
        "movie_schedules.services.cinemark.CinemarkService.get_cinema_showings_by_date"
    )
    @patch(
        "movie_schedules.services.cinepolis.CinepolisService.get_cinema_showings_by_date"
    )
    def test_get_cinema_showings_by_date(
        self, mock_cinepolis_get_showings, mock_cinemark_get_showings
    ):
        mock_cinepolis_get_showings.return_value = ShowDate(
            date=datetime(2024, 2, 5), cinemas=self.cinepolis_showings
        )
        mock_cinemark_get_showings.return_value = ShowDate(
            date=datetime(2024, 2, 5), cinemas=self.cinemark_showings
        )

        cinemark_result = self.cinema_bot.get_cinema_showings_by_date(
            "portal-nunoa", "2-febrero", "SUB"
        )

        expected_showings = ShowDate(
            date=datetime(2024, 2, 5),
            cinemas=[
                Cinema(
                    name="Cinemark",
                    movies=[
                        Movie(
                            title="Movie2",
                            showtimes=[
                                ShowTime(showtime="16:30", format="3D", seats="50")
                            ],
                        )
                    ],
                )
            ],
        )
        self.assertEqual(cinemark_result, expected_showings)

        cinepolis_result = self.cinema_bot.get_cinema_showings_by_date(
            "cinepolis-la-reina", "2-febrero", "SUB"
        )

        expected_showings = ShowDate(
            date=datetime(2024, 2, 5),
            cinemas=[
                Cinema(
                    name="Cinepolis",
                    movies=[
                        Movie(
                            title="Movie1",
                            showtimes=[
                                ShowTime(showtime="14:00", format="2D ESP", seats="100")
                            ],
                        )
                    ],
                )
            ],
        )
        self.assertEqual(cinepolis_result, expected_showings)

    @patch(
        "movie_schedules.services.cinemark.CinemarkService.get_cinema_showings_by_date_and_zone"
    )
    @patch(
        "movie_schedules.services.cinepolis.CinepolisService.get_cinema_showings_by_date_and_zone"
    )
    def test_get_cinema_showings_by_date_and_zone(
        self, mock_cinepolis_get_showings, mock_cinemark_get_showings
    ):
        mock_cinepolis_get_showings.return_value = self.cinepolis_showings
        mock_cinemark_get_showings.return_value = self.cinemark_showings

        result = self.cinema_bot.get_cinema_showings_by_date_and_zone(
            "portal-nunoa", "2-febrero", "SUB"
        )

        expected_showings = [
            Cinema(
                name="Cinepolis",
                movies=[
                    Movie(
                        title="Movie1",
                        showtimes=[
                            ShowTime(showtime="14:00", format="2D ESP", seats="100")
                        ],
                    )
                ],
            ),
            Cinema(
                name="Cinemark",
                movies=[
                    Movie(
                        title="Movie2",
                        showtimes=[ShowTime(showtime="16:30", format="3D", seats="50")],
                    )
                ],
            ),
        ]

        self.assertEqual(result, expected_showings)

    @patch(
        "movie_schedules.services.cinemark.CinemarkService.get_cinema_showings_by_zone"
    )
    @patch(
        "movie_schedules.services.cinepolis.CinepolisService.get_cinema_showings_by_zone"
    )
    def test_get_cinema_showings_by_zone(
        self, mock_cinepolis_get_showings, mock_cinemark_get_showings
    ):
        mock_cinepolis_get_showings.return_value = self.cinepolis_showings
        mock_cinemark_get_showings.return_value = self.cinemark_showings

        cinema_showings_by_zone = self.cinema_bot.get_cinema_showings_by_zone(
            "cinepolis-la-reina", "SUB"
        )

        expected_showings = [
            ShowDate(date=datetime(2024, 2, 5), cinemas=self.cinepolis_showings),
            ShowDate(date=datetime(2024, 2, 5), cinemas=self.cinemark_showings),
        ]

        self.assertEqual(cinema_showings_by_zone, expected_showings)

    """
    @patch("movie_schedules.services.cinemark.CinemarkService.get_general_cinema_showings")
    @patch("movie_schedules.services.cinepolis.CinepolisService.get_general_cinema_showings")
    def test_get_general_cinema_showings(self, mock_cinepolis_general_showings, mock_cinemark_general_showings):
        mock_cinepolis_general_showings.return_value = ("Message", 10)
        mock_cinemark_general_showings.return_value = ("Message", 5)

        message, total = self.cinema_bot.get_general_cinema_showings("Cinema", "2024-02-05", "Format")

        expected_message = "Message"
        expected_total = 15

        self.assertEqual(message, expected_message)
        self.assertEqual(total, expected_total)
    """

    @patch("movie_schedules.services.cinemark.CinemarkService.get_cinema_showings")
    @patch("movie_schedules.services.cinepolis.CinepolisService.get_cinema_showings")
    def test_get_cinema_showings(
        self, mock_cinepolis_get_showings, mock_cinemark_get_showings
    ):
        mock_cinepolis_get_showings.return_value = self.cinepolis_showings
        mock_cinemark_get_showings.return_value = self.cinemark_showings

        result_cinemark = self.cinema_bot.get_cinema_showings("portal-nunoa", "SUB")

        expected_showings = [
            Cinema(
                name="Cinemark",
                movies=[
                    Movie(
                        title="Movie2",
                        showtimes=[ShowTime(showtime="16:30", format="3D", seats="50")],
                    )
                ],
            )
        ]

        self.assertEqual(result_cinemark, expected_showings)

        result_cinepolis = self.cinema_bot.get_cinema_showings(
            "cinepolis-la-reina", "SUB"
        )

        expected_showings = [
            Cinema(
                name="Cinepolis",
                movies=[
                    Movie(
                        title="Movie1",
                        showtimes=[
                            ShowTime(showtime="14:00", format="2D ESP", seats="100")
                        ],
                    )
                ],
            )
        ]

        self.assertEqual(result_cinepolis, expected_showings)

    @patch(
        "movie_schedules.services.cinemark.CinemarkService.get_cinema_showings_by_zone"
    )
    @patch(
        "movie_schedules.services.cinepolis.CinepolisService.get_cinema_showings_by_zone"
    )
    def test_get_cinema_showings_by_zone(
        self, mock_cinepolis_get_showings, mock_cinemark_get_showings
    ):
        mock_cinepolis_get_showings.return_value = self.cinepolis_showings
        mock_cinemark_get_showings.return_value = self.cinemark_showings

        result = self.cinema_bot.get_cinema_showings_by_zone("concepción", "SUB")

        expected_showings = [
            Cinema(
                name="Cinepolis",
                movies=[
                    Movie(
                        title="Movie1",
                        showtimes=[
                            ShowTime(showtime="14:00", format="2D ESP", seats="100")
                        ],
                    )
                ],
            ),
            Cinema(
                name="Cinemark",
                movies=[
                    Movie(
                        title="Movie2",
                        showtimes=[ShowTime(showtime="16:30", format="3D", seats="50")],
                    )
                ],
            ),
        ]

        self.assertEqual(result, expected_showings)

    def test_get_movie_date_message(self):
        result = self.cinema_bot.get_movie_date_message(
            mallplaza_arica_showdates_fixture, "CINEMA"
        )
        expected_movie_date_message = (
            "2024 02 04\n\ncinemark-mallplaza-arica\n\nLOS COLONOS\n22:20 hrs — 2D SUB — 174 asientos disponibles\n——————\n\nCON TODOS MENOS CONTIGO\n21:50 hrs — 2D SUB — 182 asientos disponibles\n——————\n\nPOBRES CRIATURAS\n11:50 hrs — 2D SUB — 254 asientos disponibles\n15:00 hrs — 2D SUB — 240 asientos disponibles\n18:10 hrs — 2D SUB — 227 asientos disponibles\n21:30 hrs — 2D SUB — 256 asientos disponibles\n——————\n\nEL NIÑO Y LA GARZA\n19:00 hrs — 2D SUB — 170 asientos disponibles\n——————\n\nARGYLLE: AGENTE SECRETO\n22:30 hrs — 2D SUB — 170 asientos disponibles\n——————\n\nCHICAS PESADAS\n19:10 hrs — 2D SUB — 116 asientos disponibles\n22:00 hrs — 2D SUB — 122 asientos disponibles\n——————\n\nVIDAS PASADAS\n18:40 hrs — 2D SUB — 148 asientos disponibles\n21:20 hrs — 2D SUB — 167 asientos disponibles\n——————\n\nANATOMÍA DE UNA CAÍDA\n18:50 hrs — 2D SUB — 108 asientos disponibles\n22:10 hrs — 2D SUB — 112 asientos disponibles\n——————\n\n$SEPARATOR$2024 02 05\n\ncinemark-mallplaza-arica\n\nLOS COLONOS\n22:20 hrs — 2D SUB — 172 asientos disponibles\n——————\n\nCON TODOS MENOS CONTIGO\n21:50 hrs — 2D SUB — 191 asientos disponibles\n——————\n\nPOBRES CRIATURAS\n11:50 hrs — 2D SUB — 263 asientos disponibles\n15:00 hrs — 2D SUB — 263 asientos disponibles\n18:10 hrs — 2D SUB — 263 asientos disponibles\n21:30 hrs — 2D SUB — 261 asientos disponibles\n——————\n\nEL NIÑO Y LA GARZA\n19:00 hrs — 2D SUB — 191 asientos disponibles\n——————\n\nARGYLLE: AGENTE SECRETO\n22:30 hrs — 2D SUB — 170 asientos disponibles\n——————\n\nCHICAS PESADAS\n19:10 hrs — 2D SUB — 118 asientos disponibles\n22:00 hrs — 2D SUB — 122 asientos disponibles\n——————\n\nCALLAS PARIS 1958\n16:00 hrs — 2D SUB — 104 asientos disponibles\n——————\n\nVIDAS PASADAS\n18:40 hrs — 2D SUB — 168 asientos disponibles\n21:20 hrs — 2D SUB — 169 asientos disponibles\n——————\n\nANATOMÍA DE UNA CAÍDA\n18:50 hrs — 2D SUB — 112 asientos disponibles\n22:10 hrs — 2D SUB — 112 asientos disponibles\n——————\n\n$SEPARATOR$2024 02 06\n\ncinemark-mallplaza-arica\n\nLOS COLONOS\n22:20 hrs — 2D SUB — 174 asientos disponibles\n——————\n\nCON TODOS MENOS CONTIGO\n22:30 hrs — 2D SUB — 191 asientos disponibles\n——————\n\nPOBRES CRIATURAS\n11:50 hrs — 2D SUB — 263 asientos disponibles\n15:00 hrs — 2D SUB — 263 asientos disponibles\n18:10 hrs — 2D SUB — 263 asientos disponibles\n21:30 hrs — 2D SUB — 261 asientos disponibles\n——————\n\nARGYLLE: AGENTE SECRETO\n22:30 hrs — 2D SUB — 170 asientos disponibles\n——————\n\nCHICAS PESADAS\n19:10 hrs — 2D SUB — 120 asientos disponibles\n22:00 hrs — 2D SUB — 122 asientos disponibles\n——————\n\nVIDAS PASADAS\n18:40 hrs — 2D SUB — 166 asientos disponibles\n21:20 hrs — 2D SUB — 169 asientos disponibles\n——————\n\nANATOMÍA DE UNA CAÍDA\n18:50 hrs — 2D SUB — 110 asientos disponibles\n22:15 hrs — 2D SUB — 112 asientos disponibles\n——————\n\n$SEPARATOR$2024 02 07\n\ncinemark-mallplaza-arica\n\nLOS COLONOS\n22:20 hrs — 2D SUB — 174 asientos disponibles\n——————\n\nCON TODOS MENOS CONTIGO\n21:50 hrs — 2D SUB — 187 asientos disponibles\n——————\n\nPOBRES CRIATURAS\n11:50 hrs — 2D SUB — 263 asientos disponibles\n15:00 hrs — 2D SUB — 261 asientos disponibles\n18:10 hrs — 2D SUB — 261 asientos disponibles\n21:30 hrs — 2D SUB — 263 asientos disponibles\n——————\n\nEL NIÑO Y LA GARZA\n19:00 hrs — 2D SUB — 191 asientos disponibles\n——————\n\nARGYLLE: AGENTE SECRETO\n22:30 hrs — 2D SUB — 170 asientos disponibles\n——————\n\nCHICAS PESADAS\n19:10 hrs — 2D SUB — 120 asientos disponibles\n22:00 hrs — 2D SUB — 122 asientos disponibles\n——————\n\nVIDAS PASADAS\n18:40 hrs — 2D SUB — 169 asientos disponibles\n21:20 hrs — 2D SUB — 169 asientos disponibles\n——————\n\nANATOMÍA DE UNA CAÍDA\n18:50 hrs — 2D SUB — 112 asientos disponibles\n22:10 hrs — 2D SUB — 112 asientos disponibles\n——————\n\n$SEPARATOR$2024 02 22\n\ncinemark-mallplaza-arica\n\nTHE CHOSEN\n20:00 hrs — 2D SUB — 100 asientos disponibles\n——————\n\n$SEPARATOR$2024 02 23\n\ncinemark-mallplaza-arica\n\nTHE CHOSEN\n20:00 hrs — 2D SUB — 104 asientos disponibles\n——————\n\n$SEPARATOR$2024 02 24\n\ncinemark-mallplaza-arica\n\nTHE CHOSEN\n20:00 hrs — 2D SUB — 107 asientos disponibles\n——————\n\n$SEPARATOR$2024 02 25\n\ncinemark-mallplaza-arica\n\nTHE CHOSEN\n20:00 hrs — 2D SUB — 112 asientos disponibles\n——————\n\n$SEPARATOR$2024 02 26\n\ncinemark-mallplaza-arica\n\nTHE CHOSEN\n20:00 hrs — 2D SUB — 112 asientos disponibles\n——————\n\n$SEPARATOR$2024 02 27\n\ncinemark-mallplaza-arica\n\nTHE CHOSEN\n20:00 hrs — 2D SUB — 112 asientos disponibles\n——————\n\n$SEPARATOR$2024 02 28\n\ncinemark-mallplaza-arica\n\nTHE CHOSEN\n20:00 hrs — 2D SUB — 112 asientos disponibles\n——————\n\n$SEPARATOR$",
            63,
        )
        self.assertEqual(result, expected_movie_date_message)

    def test_check_movie_in_total(self):
        movie_title = "SOBREVIVIENTES DESPUES DEL TERREMOTO"
        is_in_total, new_total = self.cinema_bot.check_movie_in_total(movie_title, {})
        self.assertFalse(is_in_total)
        self.assertEqual(new_total, "SOBREVIVIENTES DESPUES DEL TERREMOTO")

        movie_title = "SUPER MARIO BROS"
        is_in_total, new_total = self.cinema_bot.check_movie_in_total(
            movie_title, {"SUPER MARIO BROS: LA PELÍCULA": 1}
        )
        self.assertTrue(is_in_total)
        self.assertEqual(new_total, "SUPER MARIO BROS: LA PELÍCULA")

        movie_title = "VIDAS PASADAS"
        is_in_total, new_total = self.cinema_bot.check_movie_in_total(
            movie_title, {"CHICAS PESADAS": 1}
        )
        self.assertFalse(is_in_total)
        self.assertEqual(new_total, "VIDAS PASADAS")

    @patch("movie_schedules.services.cinemark.CinemarkService.get_total")
    @patch("movie_schedules.services.cinepolis.CinepolisService.get_total")
    def test_get_total(self, mock_cinepolis_get_total, mock_cinemark_get_total):
        mock_cinepolis_get_total.return_value = sur_chile_total_fixture
        mock_cinemark_get_total.return_value = arica_total_fixture

        result = self.cinema_bot.get_total("2024-02-05", "Format")

        expected_total = """POBRES CRIATURAS: 80
CHICAS PESADAS: 47
ARGYLLE AGENTE SECRETO: 42
ANATOMIA DE UNA CAIDA: 40
VIDAS PASADAS: 40
EL NIÑO Y LA GARZA: 33
CON TODOS MENOS CONTIGO: 33
WISH EL PODER DE LOS DESEOS: 21
LOS COLONOS: 20
WONKA: 18
AQUAMAN Y EL REINO PERDIDO: 13
MASHA Y EL OSO EL DOBLE DE DIVERSION: 7
PATOS: 6
SLEEP EL MAL NO DUERME: 6
SOBREVIVIENTES DESPUES DEL TERREMOTO: 2
JACK EN LA CAJA MALDITA 3 EL ASCENSO: 2
"""

        self.assertEqual(result, expected_total)

    @patch("movie_schedules.services.cinemark.CinemarkService.get_total")
    @patch("movie_schedules.services.cinepolis.CinepolisService.get_total")
    def test_get_format_total(self, mock_cinepolis_get_total, mock_cinemark_get_total):
        mock_cinepolis_get_total.return_value = sur_chile_total_fixture
        mock_cinemark_get_total.return_value = arica_total_fixture

        result = self.cinema_bot.get_format_total("2024-02-05", "Format")

        expected_format_total = """2D SUB: 280
2D ESP: 122
4DX-2D ESP: 8
"""

        self.assertEqual(result, expected_format_total)

    @patch("movie_schedules.services.cinemark.CinemarkService.get_total")
    @patch("movie_schedules.services.cinepolis.CinepolisService.get_total")
    def test_get_cinema_total(self, mock_cinepolis_get_total, mock_cinemark_get_total):
        mock_cinepolis_get_total.return_value = sur_chile_total_fixture
        mock_cinemark_get_total.return_value = arica_total_fixture

        result = self.cinema_bot.get_cinema_total("4-febrero", "SUB")

        expected_cinema_total = """Cinépolis Paseo Costanera Puerto Montt: 25
Mallplaza Los Ángeles: 24
Plaza Maule Talca: 21
Vivo San Fernando: 20
Temuco (Edificio París): 17
Cinemark MallPlaza Arica: 14
Cinemark MallPlaza Iquique: 14
Cinemark MallPlaza La Serena: 14
Cinemark Open Ovalle: 14
Cinemark Open La Calera: 14
Cinemark Espacio Urbano: 14
Cinemark MallMarina: 14
Cinemark Alto las Condes: 14
Cinemark Portal Ñuñoa: 14
Cinemark MallPlaza Norte: 14
Cinemark MallPlaza Oeste: 14
Cinemark Mid Mall Maipú: 14
Cinemark MallPlaza Tobalaba: 14
Cinemark MallPlaza Vespucio: 14
Cinemark Open Rancagua: 14
Cinemark Mall Rancagua: 14
Cinemark MallPlaza Trebol: 14
Cinemark MallPlaza Mirador Bio-Bio: 14
Cinemark Arauco Coronel: 14
Cinemark Portal Osorno: 14
Arauco Chillán: 13
Cinépolis Paseo Chiloé: 10
"""

        self.assertEqual(result, expected_cinema_total)

    def test_get_info_cities(self):
        result = self.cinema_bot.get_info_cities()

        expected_info_cities = """antofagasta
arica
calama
chillan
chiloe
concepcion
coquimbo
coronel
gran-concepcion
iquique
la-calera
la-serena
los-angeles
norte-y-centro-de-chile
osorno
ovalle
puerto-montt
rancagua
san-fernardo
santiago
santiago-centro
santiago-norte-y-poniente
santiago-oriente
santiago-poniente
santiago-sur
sur-de-chile
talca
talcahuano
temuco
valparaiso
viña-del-mar
"""

        self.assertEqual(result, expected_info_cities)

    def test_get_info_cinemas(self):
        result = self.cinema_bot.get_info_cinemas()

        expected_info_cinemas = """alto-las-condes
arauco-chillan
arauco-coronel
arauco-estacion
arauco-maipu
arauco-quilicura
cinehoyts-espacio-urbano-antofagasta
cinemark-mallplaza-arica
cinepolis-casa-costanera
cinepolis-espacio-urbano-puente-alto
cinepolis-la-reina
cinepolis-mallplaza-egana
cinepolis-mallplaza-egana-premium-class
cinepolis-mallplaza-los-dominicos
cinepolis-mallplaza-los-dominicos-premium-class
cinepolis-ovalle
cinepolis-paseo-chiloe
cinepolis-paseo-costanera-puerto-montt
cinepolis-paseo-los-trapenses
cinepolis-patio-outlet-la-florida
cinepolis-patio-outlet-maipu
cinepolis-plazuela-independencia-puente-alto
cinepolis-shopping-quillota
cinepolis-vivo-coquimbo
cinepolis-vivo-imperio
cinepolis-vivo-outlet-temuco
espacio-urbano
espacio-urbano-melipilla
mall-marina
mall-rancagua
mallplaza-antofagasta
mallplaza-calama
mallplaza-iquique
mallplaza-la-serena
mallplaza-los-angeles
mallplaza-mirador-bio-bio
mallplaza-norte
mallplaza-oeste
mallplaza-sur
mallplaza-tobalaba
mallplaza-trebol
mallplaza-vespucio
mid-mall-maipu
open-la-calera
open-ovalle
open-rancagua
parque-arauco
parque-arauco-premium-class
paseo-los-dominicos-(san-carlos)
paseo-san-bernardo
plaza-maule-talca
portal-nunoa
portal-osorno
temuco-(edificio-paris)
valparaiso
vivo-san-fernando
"""
        self.assertEqual(result, expected_info_cinemas)
