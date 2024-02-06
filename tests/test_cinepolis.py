import json
import unittest
from unittest.mock import patch

from movie_schedules.dataclasses.cinema import Cinema
from movie_schedules.dataclasses.movie import Movie, ShowTime
from movie_schedules.services.cinepolis import CinepolisService
from tests.fixtures.cinepolis_expected_results import (
    chillan_total_fixture, cinepolis_fixture, showtimes_by_date_fixture,
    sur_de_chile_formatted_showings_fixture)


class TestCinepolisService(unittest.TestCase):
    def setUp(self):
        self.cinepolis_service = CinepolisService()

    @patch("movie_schedules.services.cinepolis.requests.post")
    def test_get_cinemas_from_zone(self, mock_post):
        # Add your test logic here
        pass

    @patch("movie_schedules.services.cinepolis.requests.post")
    def test_get_zone_by_cinema(self, mock_post):
        # Add your test logic here
        pass

    @patch("movie_schedules.services.cinepolis.requests.post")
    def test_is_chain(self, mock_post):
        # Add your test logic here
        pass

    @patch("movie_schedules.services.cinepolis.requests.post")
    def test_get_showings_response_by_zone(self, mock_post):
        mock_post.return_value.json.return_value = cinepolis_fixture

        response = self.cinepolis_service.get_showings_response_by_zone("sur-de-chile")

        self.assertEqual(response, cinepolis_fixture["d"]["Cinemas"])

    @patch("movie_schedules.services.cinepolis.requests.post")
    def test_get_cinemas_by_zone(self, mock_post):
        # Add your test logic here
        pass

    @patch("movie_schedules.services.cinepolis.requests.post")
    def test_get_only_showings_from_cinemas(self, mock_post):
        # Add your test logic here
        pass

    @patch("movie_schedules.services.cinepolis.requests.post")
    def test_get_cinema_by_cinema_key(self, mock_post):
        # Add your test logic here
        pass

    @patch("movie_schedules.services.cinepolis.requests.post")
    def test_get_cinema_by_cinemas_and_cinema_key(self, mock_post):
        cinemas = [{"Key": "1", "Name": "Cinema1"}, {"Key": "2", "Name": "Cinema2"}]
        cinema_key = "1"

        result = self.cinepolis_service.get_cinema_by_cinemas_and_cinema_key(
            cinemas, cinema_key
        )

        self.assertEqual(result, {"Key": "1", "Name": "Cinema1"})

    @patch("movie_schedules.services.cinepolis.requests.post")
    def test_get_showtimes_by_date(self, mock_post):
        cinemas = cinepolis_fixture["d"]["Cinemas"][0]

        result = self.cinepolis_service.get_showtimes_by_date(
            cinemas, date_name="4 febrero"
        )

        self.assertEqual(result, showtimes_by_date_fixture)

    def test_get_movie_showings(self):
        # Add your test logic here
        pass

    def test_get_formatted_format(self):
        self.assertEqual(self.cinepolis_service.get_formatted_format("ESP"), "2D ESP")
        self.assertEqual(self.cinepolis_service.get_formatted_format("SUBT"), "2D SUB")
        self.assertEqual(
            self.cinepolis_service.get_formatted_format("2D DOB"), "2D ESP"
        )
        self.assertEqual(
            self.cinepolis_service.get_formatted_format("2D SUBT"), "2D SUB"
        )

    def test_get_showtimes(self):
        # Add your test logic here
        pass

    @patch("movie_schedules.services.cinepolis.requests.post")
    def test_get_formatted_showings_by_cinema(self, mock_post):
        mock_post.return_value.json.return_value = cinepolis_fixture

        zone_showings = self.cinepolis_service.get_showings_response_by_zone(
            "sur-de-chile"
        )

        result = self.cinepolis_service.get_formatted_showings_by_cinema(
            zone_showings=zone_showings,
            cinema_key="arauco-chillan",
            date="4-febrero",
            movie="vidas-pasadas",
            format="SUB",
        )
        formatted_showings_fixture = Cinema(
            name="Arauco Chillán",
            movies=[
                Movie(
                    title="VIDAS PASADAS",
                    showtimes=[ShowTime(showtime="17:15", format="2D SUB", seats="")],
                )
            ],
        )

        self.assertEqual(result, formatted_showings_fixture)

    @patch("movie_schedules.services.cinepolis.requests.post")
    def test_get_cinema_showings(self, mock_post):
        # Add your test logic here
        pass

    @patch("movie_schedules.services.cinepolis.requests.post")
    def test_get_cinema_showings_by_zone(self, mock_post):
        # Add your test logic here
        pass

    @patch("movie_schedules.services.cinepolis.requests.post")
    def test_get_cinema_showings_by_date(self, mock_post):
        # Add your test logic here
        pass

    @patch("movie_schedules.services.cinepolis.requests.post")
    def test_get_cinema_showings_by_date_and_zone(self, mock_post):
        # Add your test logic here
        pass

    @patch("movie_schedules.services.cinepolis.requests.post")
    def test_get_total(self, mock_post):
        mock_post.return_value.json.return_value = cinepolis_fixture

        result = self.cinepolis_service.get_total("4-febrero", "2D ESP")

        self.assertEqual(result, chillan_total_fixture)
