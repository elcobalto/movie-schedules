import unittest
from datetime import datetime
from unittest.mock import MagicMock, patch

from movie_schedules.dataclasses.cinema import Cinema, ShowDate
from movie_schedules.dataclasses.movie import Movie, ShowTime
from movie_schedules.services.cinemark import CinemarkService
from tests.fixtures.cinemark_expected_results import (
    arica_cinema_showings_fixture, arica_showdates_february_fixture,
    arica_showdates_fixture, arica_total_fixture, arica_wonka_showings_fixture,
    cinemark_fixture, mallplaza_airca_wonka_showings_fixture,
    mallplaza_arica_movie_showtimes, mallplaza_arica_showdates_fixture,
    wonka_february_showings_fixture)


class TestCinemarkService(unittest.TestCase):
    def setUp(self):
        self.cinemark_service = CinemarkService()

    def test_is_chain(self):
        self.assertTrue(self.cinemark_service.is_chain("cinemark-mallplaza-arica"))
        self.assertFalse(self.cinemark_service.is_chain("cinepolis-la-reina"))

    def test_get_cinemas_from_zone(self):
        result = self.cinemark_service.get_cinemas_from_zone("arica")

        self.assertEqual(
            result,
            [
                {
                    "name": "Cinemark MallPlaza Arica",
                    "tag": "cinemark-mallplaza-arica",
                    "id": 2305,
                }
            ],
        )

    def test_get_cinema_by_cinema_key(self):
        result = self.cinemark_service.get_cinema_by_cinema_key(
            "cinemark-mallplaza-arica"
        )
        print(result)

        self.assertEqual(
            result,
            {
                "name": "Cinemark MallPlaza Arica",
                "tag": "cinemark-mallplaza-arica",
                "id": 2305,
            },
        )

    @patch("movie_schedules.services.cinemark.requests.get")
    def test_get_showings_response_by_zone(self, mock_get):
        mock_get.return_value.json.return_value = cinemark_fixture

        result = self.cinemark_service.get_showings_response_by_zone(cinema_id=512)

        self.assertEqual(result, cinemark_fixture)

    def test_check_date(self):
        date = "4-febrero"
        dateshow = {"date": "2024-02-04"}
        result = self.cinemark_service.check_date(date, dateshow)

        self.assertTrue(result)

    def test_format_movieshow_title(self):
        result = self.cinemark_service.format_movieshow_title("Wonka Movie")

        self.assertEqual(result, "wonka-movie")

    def test_check_similar_titles(self):
        self.assertTrue(
            self.cinemark_service.check_similar_titles("Wonka", "Wonka: La Película")
        )
        self.assertFalse(
            self.cinemark_service.check_similar_titles("Vidas Pasadas", "El Pasado")
        )

    def test_format_show_format(self):
        result = self.cinemark_service.format_show_format("Wonka (2D DOB)")

        self.assertEqual(result, "2D ESP")

    @patch("movie_schedules.services.cinemark.requests.get")
    def test_get_movie_showtimes(self, mock_get):
        mock_get.return_value.json.return_value = cinemark_fixture

        movie_title = "wonka"
        movie_showings = self.cinemark_service.get_showings_response_by_zone(
            cinema_id=2305
        )
        result = self.cinemark_service.get_movie_showtimes(
            movie_title, movie_showings[0]["movies"][0], "ESP"
        )

        self.assertEqual(len(result.showtimes), 2)
        self.assertEqual(result.showtimes[0].format, "2D ESP")
        self.assertEqual(
            result,
            Movie(
                title="wonka",
                showtimes=[
                    ShowTime(showtime="13:20", format="2D ESP", seats=112),
                    ShowTime(showtime="16:00", format="2D ESP", seats=109),
                ],
            ),
        )

    @patch("movie_schedules.services.cinemark.requests.get")
    def test_get_formatted_movie_showings(self, mock_get):
        mock_get.return_value.json.return_value = cinemark_fixture

        movie_showings = self.cinemark_service.get_showings_response_by_zone(
            cinema_id=2305
        )
        result = self.cinemark_service.get_formatted_movie_showings(
            movie_showings[0]["movies"], "wonka", "ESP"
        )

        self.assertEqual(len(result), 1)
        self.assertEqual(
            result,
            [
                Movie(
                    title="wonka",
                    showtimes=[
                        ShowTime(showtime="13:20", format="2D ESP", seats=112),
                        ShowTime(showtime="16:00", format="2D ESP", seats=109),
                    ],
                )
            ],
        )

    @patch("movie_schedules.services.cinemark.requests.get")
    def test_get_showings(self, mock_get):
        mock_get.return_value.json.return_value = cinemark_fixture

        result = self.cinemark_service.get_showings(
            "wonka", "4-febrero", "cinemark-mallplaza-arica", "ESP"
        )

        self.assertIsInstance(result, ShowDate)
        self.assertEqual(len(result.cinemas), 1)
        self.assertEqual(
            result,
            ShowDate(
                date="4-febrero",
                cinemas=[
                    Cinema(
                        name="Cinemark MallPlaza Arica",
                        movies=[
                            Movie(
                                title="wonka",
                                showtimes=[
                                    ShowTime(
                                        showtime="13:20", format="2D ESP", seats=112
                                    ),
                                    ShowTime(
                                        showtime="16:00", format="2D ESP", seats=109
                                    ),
                                ],
                            )
                        ],
                    )
                ],
            ),
        )

    def test_get_cinemas_by_zone(self):
        result = self.cinemark_service.get_cinemas_by_zone("arica")

        self.assertEqual(
            result,
            [
                {
                    "name": "Cinemark MallPlaza Arica",
                    "tag": "cinemark-mallplaza-arica",
                    "id": 2305,
                }
            ],
        )

    @patch("movie_schedules.services.cinemark.requests.get")
    def test_get_showings_by_cinema(self, mock_get):
        mock_get.return_value.json.return_value = cinemark_fixture

        cinema = {"id": 2305, "name": "cinemark-mallplaza-arica"}
        result = self.cinemark_service.get_showings_by_cinema(
            "4-febrero", cinema, "wonka", "ESP"
        )

        self.assertEqual(len(result), 1)
        self.assertEqual(
            result,
            [
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
        )

    @patch("movie_schedules.services.cinemark.requests.get")
    def test_get_showings_by_cinema_tags(self, mock_get):
        mock_get.return_value.json.return_value = cinemark_fixture

        cinemas = [{"id": 2305, "name": "cinemark-mallplaza-arica"}]
        result = self.cinemark_service.get_showings_by_cinema_tags(
            "wonka", "4-febrero", cinemas, "ESP"
        )
        print(result)

        self.assertEqual(len(result), 1)
        self.assertEqual(
            result,
            [
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
        )

    @patch("movie_schedules.services.cinemark.requests.get")
    def test_get_showings_by_zone(self, mock_get):
        mock_get.return_value.json.return_value = cinemark_fixture

        result = self.cinemark_service.get_showings_by_zone(
            "wonka", "4-febrero", "arica", "ESP"
        )

        self.assertEqual(len(result), 1)
        self.assertEqual(
            result,
            [
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
        )

    @patch("movie_schedules.services.cinemark.requests.get")
    def test_get_showing_by_date(self, mock_get):
        mock_get.return_value.json.return_value = cinemark_fixture

        result = self.cinemark_service.get_showing_by_date("wonka", "4-febrero", "ESP")

        self.assertEqual(len(result), 20)
        self.assertEqual(result, wonka_february_showings_fixture)

    @patch("movie_schedules.services.cinemark.requests.get")
    def test_get_showing_by_cinema(self, mock_get):
        mock_get.return_value.json.return_value = cinemark_fixture

        cinema = {"id": 2305, "name": "cinemark-mallplaza-arica"}
        result = self.cinemark_service.get_showing_by_cinema("wonka", cinema, "ESP")

        self.assertEqual(len(result), 11)
        self.assertEqual(
            result,
            mallplaza_airca_wonka_showings_fixture,
        )

    @patch("movie_schedules.services.cinemark.requests.get")
    def test_get_showing_by_zone(self, mock_get):
        mock_get.return_value.json.return_value = cinemark_fixture
        result = self.cinemark_service.get_showing_by_zone("wonka", "arica", "ESP")

        self.assertEqual(len(result), 11)
        self.assertEqual(
            result,
            arica_wonka_showings_fixture,
        )

    @patch("movie_schedules.services.cinemark.requests.get")
    def test_get_movie_showtimes_for_movie_showings(self, mock_get):
        mock_get.return_value.json.return_value = cinemark_fixture

        dateshow = self.cinemark_service.get_showings_response_by_zone(2305)[0]
        result = self.cinemark_service.get_movie_showtimes_for_movie_showings(
            dateshow, "SUB"
        )

        self.assertEqual(len(result), 12)
        self.assertEqual(result, mallplaza_arica_movie_showtimes)

    @patch("movie_schedules.services.cinemark.requests.get")
    def test_get_cinema_showings(self, mock_get):
        mock_get.return_value.json.return_value = cinemark_fixture

        cinema = {"id": 2305, "name": "cinemark-mallplaza-arica"}
        result = self.cinemark_service.get_cinema_showings(cinema, "SUB")

        self.assertEqual(len(result), 11)
        self.assertEqual(
            result,
            mallplaza_arica_showdates_fixture,
        )

    @patch("movie_schedules.services.cinemark.requests.get")
    def test_get_cinema_showings_by_zone(self, mock_get):
        mock_get.return_value.json.return_value = cinemark_fixture

        result = self.cinemark_service.get_cinema_showings_by_zone("arica", "SUB")

        self.assertEqual(len(result), 11)
        self.assertEqual(
            result,
            arica_showdates_fixture,
        )

    @patch("movie_schedules.services.cinemark.requests.get")
    def test_get_cinema_showings_by_date(self, mock_get):
        mock_get.return_value.json.return_value = cinemark_fixture

        cinema = self.cinemark_service.get_cinemas_from_zone("arica")[0]
        result = self.cinemark_service.get_cinema_showings_by_date(
            cinema, "4-febrero", "SUB"
        )

        self.assertIsInstance(result, ShowDate)
        self.assertEqual(
            result,
            arica_showdates_february_fixture,
        )
        self.assertEqual(len(result.cinemas), 1)

    @patch("movie_schedules.services.cinemark.requests.get")
    def test_get_cinema_showings_by_date_and_zone(self, mock_get):
        mock_get.return_value.json.return_value = cinemark_fixture

        result = self.cinemark_service.get_cinema_showings_by_date_and_zone(
            "arica", "4-febrero", "SUB"
        )

        self.assertEqual(len(result), 1)
        self.assertEqual(
            result,
            arica_cinema_showings_fixture,
        )

    @patch("movie_schedules.services.cinemark.requests.get")
    def test_get_total(self, mock_get):
        mock_get.return_value.json.return_value = cinemark_fixture

        result = self.cinemark_service.get_total("4-febrero", "SUB")

        self.assertEqual(len(result), 20)
        self.assertEqual(result, arica_total_fixture)
