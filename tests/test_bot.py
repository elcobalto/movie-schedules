import unittest
from datetime import datetime
from unittest.mock import patch

from movie_schedules.dataclasses.cinema import Cinema, ShowDate
from movie_schedules.dataclasses.movie import Movie, ShowTime
from movie_schedules.services.bot import \
    CinemaBot  # Update with the actual import path


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

    """
    @patch("movie_schedules.services.cinemark.CinemarkService.get_showings")
    def test_get_showings_cinepolis(self, mock_cinepolis_get_showings):
        mock_cinepolis_get_showings.return_value = self.cinepolis_showings

        showings = self.cinema_bot.get_showings("Movie1", "2024-02-05", "Cinepolis", "2D ESP")

        self.assertEqual(showings, ShowDate(date=datetime.now().date(), cinemas=self.cinepolis_showings))

    @patch("movie_schedules.services.cinepolis.CinepolisService.get_showings")
    def test_get_showings_cinemark(self, mock_cinemark_get_showings):
        mock_cinemark_get_showings.return_value = self.cinemark_showings

        showings = self.cinema_bot.get_showings("Movie2", "2024-02-05", "Cinemark", "3D")

        self.assertEqual(showings, ShowDate(date=datetime.now().date(), cinemas=self.cinemark_showings))

    @patch("movie_schedules.services.cinemark.CinemarkService.get_showings_by_zone")
    @patch("movie_schedules.services.cinepolis.CinepolisService.get_showings_by_zone")
    def test_get_showings_by_zone(self, mock_cinepolis_get_showings, mock_cinemark_get_showings):
        mock_cinepolis_get_showings.return_value = self.cinepolis_showings
        mock_cinemark_get_showings.return_value = self.cinemark_showings

        showings_by_zone = self.cinema_bot.get_showings_by_zone("Movie", "2024-02-05", "Cinema", "Format")

        expected_showings = ShowDate(date=datetime.now().date(), cinemas=self.cinepolis_showings + self.cinemark_showings)

        self.assertEqual(showings_by_zone, expected_showings)

    @patch("movie_schedules.services.cinemark.CinemarkService.get_showing_by_date")
    @patch("movie_schedules.services.cinepolis.CinepolisService.get_showing_by_date")
    def test_get_showing_by_date(self, mock_cinepolis_get_showing, mock_cinemark_get_showing):
        mock_cinepolis_get_showing.return_value = self.cinepolis_showings
        mock_cinemark_get_showing.return_value = self.cinemark_showings

        showing_by_date = self.cinema_bot.get_showing_by_date("Movie", "2024-02-05", "Format")

        expected_showings = ShowDate(date=datetime.now().date(), cinemas=self.cinepolis_showings + self.cinemark_showings)

        self.assertEqual(showing_by_date, expected_showings)

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

    @patch("movie_schedules.services.cinemark.CinemarkService.get_showing_by_cinema")
    @patch("movie_schedules.services.cinepolis.CinepolisService.get_showing_by_cinema")
    def test_get_showing_by_cinema(self, mock_cinepolis_get_showing, mock_cinemark_get_showing):
        mock_cinepolis_get_showing.return_value = self.cinepolis_showings
        mock_cinemark_get_showing.return_value = self.cinemark_showings

        showings_by_cinema = self.cinema_bot.get_showing_by_cinema("Movie", "Cinema", "Format")

        expected_showings = [
            ShowDate(date=datetime.now().date(), cinemas=self.cinepolis_showings),
            ShowDate(date=datetime.now().date(), cinemas=self.cinemark_showings),
        ]

        self.assertEqual(showings_by_cinema, expected_showings)

    @patch("movie_schedules.services.cinemark.CinemarkService.get_cinema_showings_by_date")
    @patch("movie_schedules.services.cinepolis.CinepolisService.get_cinema_showings_by_date")
    def test_get_cinema_showings_by_date(self, mock_cinepolis_get_showings, mock_cinemark_get_showings):
        mock_cinepolis_get_showings.return_value = self.cinepolis_showings
        mock_cinemark_get_showings.return_value = self.cinemark_showings

        cinema_showings_by_date = self.cinema_bot.get_cinema_showings_by_date("Cinema", "2024-02-05", "Format")

        expected_showings = ShowDate(date=datetime.now().date(), cinemas=self.cinepolis_showings + self.cinemark_showings)

        self.assertEqual(cinema_showings_by_date, expected_showings)

    @patch("movie_schedules.services.cinemark.CinemarkService.get_cinema_showings_by_date_and_zone")
    @patch("movie_schedules.services.cinepolis.CinepolisService.get_cinema_showings_by_date_and_zone")
    def test_get_cinema_showings_by_date_and_zone(self, mock_cinepolis_get_showings, mock_cinemark_get_showings):
        mock_cinepolis_get_showings.return_value = self.cinepolis_showings
        mock_cinemark_get_showings.return_value = self.cinemark_showings

        cinema_showings_by_date_and_zone = self.cinema_bot.get_cinema_showings_by_date_and_zone("Cinema", "2024-02-05", "Format")

        expected_showings = [
            ShowDate(date=datetime.now().date(), cinemas=self.cinepolis_showings),
            ShowDate(date=datetime.now().date(), cinemas=self.cinemark_showings),
        ]

        self.assertEqual(cinema_showings_by_date_and_zone, expected_showings)

    @patch("movie_schedules.services.cinemark.CinemarkService.get_cinema_showings")
    @patch("movie_schedules.services.cinepolis.CinepolisService.get_cinema_showings")
    def test_get_cinema_showings(self, mock_cinepolis_get_showings, mock_cinemark_get_showings):
        mock_cinepolis_get_showings.return_value = self.cinepolis_showings
        mock_cinemark_get_showings.return_value = self.cinemark_showings

        cinema_showings = self.cinema_bot.get_cinema_showings("Cinema", "Format")

        expected_showings = [
            ShowDate(date=datetime.now().date(), cinemas=self.cinepolis_showings),
            ShowDate(date=datetime.now().date(), cinemas=self.cinemark_showings),
        ]

        self.assertEqual(cinema_showings, expected_showings)

    @patch("movie_schedules.services.cinemark.CinemarkService.get_cinema_showings_by_zone")
    @patch("movie_schedules.services.cinepolis.CinepolisService.get_cinema_showings_by_zone")
    def test_get_cinema_showings_by_zone(self, mock_cinepolis_get_showings, mock_cinemark_get_showings):
        mock_cinepolis_get_showings.return_value = self.cinepolis_showings
        mock_cinemark_get_showings.return_value = self.cinemark_showings

        cinema_showings_by_zone = self.cinema_bot.get_cinema_showings_by_zone("Cinema", "Format")

        expected_showings = [
            ShowDate(date=datetime.now().date(), cinemas=self.cinepolis_showings),
            ShowDate(date=datetime.now().date(), cinemas=self.cinemark_showings),
        ]

        self.assertEqual(cinema_showings_by_zone, expected_showings)

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


    @patch("movie_schedules.services.cinemark.CinemarkService.get_cinema_showings")
    @patch("movie_schedules.services.cinepolis.CinepolisService.get_cinema_showings")
    def test_get_cinema_showings(self, mock_cinepolis_get_showings, mock_cinemark_get_showings):
        mock_cinepolis_get_showings.return_value = self.cinepolis_showings
        mock_cinemark_get_showings.return_value = self.cinemark_showings

        cinema_showings = self.cinema_bot.get_cinema_showings("Cinema", "Format")

        expected_showings = [
            ShowDate(date=datetime.now().date(), cinemas=self.cinepolis_showings),
            ShowDate(date=datetime.now().date(), cinemas=self.cinemark_showings),
        ]

        self.assertEqual(cinema_showings, expected_showings)

    @patch("movie_schedules.services.cinemark.CinemarkService.get_cinema_showings_by_zone")
    @patch("movie_schedules.services.cinepolis.CinepolisService.get_cinema_showings_by_zone")
    def test_get_cinema_showings_by_zone(self, mock_cinepolis_get_showings, mock_cinemark_get_showings):
        mock_cinepolis_get_showings.return_value = self.cinepolis_showings
        mock_cinemark_get_showings.return_value = self.cinemark_showings

        cinema_showings_by_zone = self.cinema_bot.get_cinema_showings_by_zone("Cinema", "Format")

        expected_showings = [
            ShowDate(date=datetime.now().date(), cinemas=self.cinepolis_showings),
            ShowDate(date=datetime.now().date(), cinemas=self.cinemark_showings),
        ]

        self.assertEqual(cinema_showings_by_zone, expected_showings)

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

    @patch("movie_schedules.services.cinemark.CinemarkService.get_total")
    @patch("movie_schedules.services.cinepolis.CinepolisService.get_total")
    def test_get_total(self, mock_cinepolis_get_total, mock_cinemark_get_total):
        mock_cinepolis_get_total.return_value = "Cinepolis Total"
        mock_cinemark_get_total.return_value = "Cinemark Total"

        total = self.cinema_bot.get_total("2024-02-05", "Format")

        expected_total = "Cinepolis TotalCinemark Total"

        self.assertEqual(total, expected_total)

    @patch("movie_schedules.services.cinemark.CinemarkService.get_format_total")
    @patch("movie_schedules.services.cinepolis.CinepolisService.get_format_total")
    def test_get_format_total(self, mock_cinepolis_get_total, mock_cinemark_get_total):
        mock_cinepolis_get_total.return_value = "Cinepolis Format Total"
        mock_cinemark_get_total.return_value = "Cinemark Format Total"

        format_total = self.cinema_bot.get_format_total("2024-02-05", "Format")

        expected_format_total = "Cinepolis Format TotalCinemark Format Total"

        self.assertEqual(format_total, expected_format_total)

    @patch("movie_schedules.services.cinemark.CinemarkService.get_cinema_total")
    @patch("movie_schedules.services.cinepolis.CinepolisService.get_cinema_total")
    def test_get_cinema_total(self, mock_cinepolis_get_total, mock_cinemark_get_total):
        mock_cinepolis_get_total.return_value = "Cinepolis Cinema Total"
        mock_cinemark_get_total.return_value = "Cinemark Cinema Total"

        cinema_total = self.cinema_bot.get_cinema_total("2024-02-05", "Format")

        expected_cinema_total = "Cinepolis Cinema TotalCinemark Cinema Total"

        self.assertEqual(cinema_total, expected_cinema_total)

    @patch("movie_schedules.services.cinemark.CinemarkService.get_info_cities")
    @patch("movie_schedules.services.cinepolis.CinepolisService.get_info_cities")
    def test_get_info_cities(self, mock_cinepolis_info_cities, mock_cinemark_info_cities):
        mock_cinepolis_info_cities.return_value = "Cinepolis Cities Info"
        mock_cinemark_info_cities.return_value = "Cinemark Cities Info"

        info_cities = self.cinema_bot.get_info_cities()

        expected_info_cities = "Cinepolis Cities InfoCinemark Cities Info"

        self.assertEqual(info_cities, expected_info_cities)

    @patch("movie_schedules.services.cinemark.CinemarkService.get_info_cinemas")
    @patch("movie_schedules.services.cinepolis.CinepolisService.get_info_cinemas")
    def test_get_info_cinemas(self, mock_cinepolis_info_cinemas, mock_cinemark_info_cinemas):
        mock_cinepolis_info_cinemas.return_value = "Cinepolis Cinemas Info"
        mock_cinemark_info_cinemas.return_value = "Cinemark Cinemas Info"

        info_cinemas = self.cinema_bot.get_info_cinemas()

        expected_info_cinemas = "Cinepolis Cinemas InfoCinemark Cinemas Info"

        self.assertEqual(info_cinemas, expected_info_cinemas)
    """
