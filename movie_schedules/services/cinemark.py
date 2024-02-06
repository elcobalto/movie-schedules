from typing import Any, Dict, List, Optional

import requests

from movie_schedules.constants.cinemark import (CINEMA_MACROZONES,
                                                CINEMA_ZONES,
                                                CINEMA_ZONES_TAGS,
                                                CINEMAS_TAGS,
                                                TOTAL_CINEMAS_TAGS)
from movie_schedules.dataclasses.cinema import Cinema, ShowDate
from movie_schedules.dataclasses.movie import Movie, ShowTime
from movie_schedules.services.main import CinemaService

month_to_number = {
    "enero": "01",
    "febrero": "02",
    "marzo": "03",
    "abril": "04",
    "mayo": "05",
    "junio": "06",
    "julio": "07",
    "agosto": "08",
    "septiembre": "09",
    "octubre": "10",
    "noviembre": "11",
    "diciembre": "12",
}


class CinemarkService(CinemaService):
    name = ""
    host = "https://api.cinemark.cl/api/"

    def is_chain(self, cinema: str) -> bool:
        return cinema in CINEMAS_TAGS or cinema in CINEMA_ZONES_TAGS

    def get_cinemas_from_zone(self, zone_name: str) -> List[Dict[str, Any]]:
        for cinema_zone in CINEMA_ZONES:
            if zone_name == cinema_zone["tag"]:
                return cinema_zone["list"]
        return []

    def get_cinema_by_cinema_key(self, cinema_name: str) -> Optional[Dict[str, Any]]:
        for zone in CINEMA_ZONES:
            cinemas_in_zone = zone["list"]
            for cinema in cinemas_in_zone:
                if cinema_name == cinema["tag"]:
                    return cinema
        return None

    def get_showings_response_by_zone(
        self,
        cinema_id: int = 512,
    ) -> List[Dict[str, Any]]:
        try:
            showings = requests.get(
                f"{self.host}/vista/data/billboard?cinema_id={cinema_id}"
            )
            clean_showings = showings.json()
            return clean_showings
        except Exception:
            return []

    def check_date(self, date: str, dateshow: Dict[str, Any]) -> bool:
        listed_date = date.split("-")
        listed_dateshow = dateshow["date"].split("-")
        month_date = listed_date[1]
        try:
            month = int(month_date)
        except Exception:
            month = month_to_number[month_date]
        return int(month) == int(listed_dateshow[1]) and int(listed_date[0]) == int(
            listed_dateshow[2]
        )

    def format_movieshow_title(self, movie_title: str) -> str:
        return movie_title.lower().replace(" ", "-")

    def check_similar_titles(self, movie: str, movie_title: str) -> bool:
        return movie_title in movie or movie in movie_title

    def format_show_format(self, showformat: str) -> str:
        return (
            showformat.split("(")[1][:-1].replace("DOB", "ESP").replace("SUBT", "SUB")
        )

    def get_movie_showtimes(
        self, movie_title: str, movie_showing: Dict[str, Any], format: str
    ) -> Movie:
        movie_formats = movie_showing["movie_versions"]
        showtimes = []
        for show_format in movie_formats:
            format_name = self.format_show_format(show_format["title"])
            if format and format not in format_name:
                continue
            for timeshow in show_format["sessions"]:
                showtime = timeshow["hour"]
                showtimes.append(
                    ShowTime(
                        showtime=showtime[:-3],
                        format=format_name,
                        seats=timeshow["seats_available"],
                    )
                )
        return Movie(title=movie_title, showtimes=showtimes)

    def get_formatted_movie_showings(
        self,
        movie_showings: List[Dict[str, Any]],
        movie: str,
        format: str,
    ) -> List[Movie]:
        movies = []
        for movie_showing in movie_showings:
            movie_title = self.format_movieshow_title(movie_showing["title"])
            if movie and not self.check_similar_titles(movie, movie_title):
                continue
            movies.append(self.get_movie_showtimes(movie_title, movie_showing, format))
        return movies

    def get_showings(
        self, movie: str, date: str, cinema_name: str, format: str
    ) -> ShowDate:
        cinema = self.get_cinema_by_cinema_key(cinema_name)
        dateshows = self.get_showings_response_by_zone(cinema["id"])
        cinemas = []
        for dateshow in dateshows:
            is_date = self.check_date(date, dateshow)
            if not is_date:
                continue
            cinemas.append(
                Cinema(
                    name=cinema["name"],
                    movies=self.get_formatted_movie_showings(
                        dateshow["movies"], movie, format
                    ),
                )
            )
        return ShowDate(date=date, cinemas=cinemas)

    def get_cinemas_by_zone(self, zone: str) -> List[Dict[str, Any]]:
        for cinema_zone in CINEMA_ZONES:
            if cinema_zone["tag"] == zone:
                return cinema_zone["list"]
        return []

    def get_showings_by_cinema(
        self, date: str, cinema: Dict[str, Any], movie: str, format: str
    ) -> List[Cinema]:
        dateshows = self.get_showings_response_by_zone(cinema["id"])
        cinemas = []
        for dateshow in dateshows:
            is_date = self.check_date(date, dateshow)
            if not is_date:
                continue
            movies = self.get_formatted_movie_showings(
                dateshow["movies"], movie, format
            )
            cinemas.append(
                Cinema(
                    name=cinema["name"],
                    movies=movies,
                )
            )
        return cinemas

    def get_showings_by_cinema_tags(
        self, movie: str, date: str, cinemas: List[Dict[str, Any]], format: str
    ):
        cinemas_showdates = []
        for cinema in cinemas:
            cinemas_showdates += self.get_showings_by_cinema(
                date, cinema, movie, format
            )
        return cinemas_showdates

    def get_showings_by_zone(
        self, movie: str, date: str, zone: str, format: str
    ) -> List[Cinema]:
        return self.get_showings_by_cinema_tags(
            movie, date, self.get_cinemas_by_zone(zone), format
        )

    def get_showing_by_date(self, movie: str, date: str, format: str) -> List[Cinema]:
        cinemas = []
        for cinema_macrozone in CINEMA_MACROZONES:
            cinemas += cinema_macrozone["list"]
        return self.get_showings_by_cinema_tags(movie, date, cinemas, format)

    def get_showing_by_cinema(
        self, movie: str, cinema: Dict[str, Any], format: str = None
    ) -> List[ShowDate]:
        dateshows = self.get_showings_response_by_zone(cinema["id"])
        showdates = []
        for dateshow in dateshows:
            movies = self.get_formatted_movie_showings(
                dateshow["movies"], movie, format
            )
            showdates.append(
                ShowDate(
                    date=dateshow["date"],
                    cinemas=[Cinema(name=cinema["name"], movies=movies)],
                )
            )
        return showdates

    def get_showing_by_zone(
        self, movie: str, zone_name: str, format: str = None
    ) -> List[ShowDate]:
        cinemas = self.get_cinemas_from_zone(zone_name)
        total_showings = []
        for cinema in cinemas:
            total_showings += self.get_showing_by_cinema(movie, cinema, format)
        return total_showings

    def get_movie_showtimes_for_movie_showings(
        self, dateshow: Dict, format: str
    ) -> List[Movie]:
        movie_showtimes = []
        for movie_showing in dateshow["movies"]:
            movie_title = self.format_movieshow_title(movie_showing["title"])
            movie_showtimes.append(
                self.get_movie_showtimes(movie_title, movie_showing, format)
            )
        return movie_showtimes

    def get_cinema_showings(
        self, cinema: Dict[str, Any], format: str
    ) -> List[ShowDate]:
        dateshows = self.get_showings_response_by_zone(cinema["id"])
        showdates = []
        for dateshow in dateshows:
            movies = self.get_movie_showtimes_for_movie_showings(dateshow, format)
            showdates.append(
                ShowDate(
                    date=dateshow["date"],
                    cinemas=[Cinema(name=cinema["name"], movies=movies)],
                )
            )
        return showdates

    def get_cinema_showings_by_zone(
        self, zone_name: str, format: str
    ) -> List[ShowDate]:
        cinemas = self.get_cinemas_from_zone(zone_name)
        total_showings = []
        for cinema in cinemas:
            total_showings += self.get_cinema_showings(cinema, format)
        return total_showings

    def get_cinema_showings_by_date(
        self, cinema: Dict[str, Any], date: str, format: str
    ) -> ShowDate:
        dateshows = self.get_showings_response_by_zone(cinema["id"])
        movies = []
        for dateshow in dateshows:
            is_date = self.check_date(date, dateshow)
            if not is_date:
                continue
            movies += self.get_movie_showtimes_for_movie_showings(dateshow, format)
        return ShowDate(
            date=dateshows[0]["date"],
            cinemas=[Cinema(name=cinema["name"], movies=movies)],
        )

    def get_cinema_showings_by_date_and_zone(
        self, zone_name: str, date: str, format: str
    ) -> List[ShowDate]:
        cinemas = self.get_cinemas_from_zone(zone_name)
        total_showings = []
        for cinema in cinemas:
            total_showings.append(
                self.get_cinema_showings_by_date(cinema, date, format)
            )
        return total_showings

    def get_total(self, date: str, format: str) -> List[Cinema]:
        """
        Get the total showdates for every cinema within an specific date and format
        """
        cinemas_showdates = []
        for cinema_tag in TOTAL_CINEMAS_TAGS:
            cinema = self.get_cinema_by_cinema_key(cinema_tag)
            cinemas_showdates += self.get_showings_by_cinema(date, cinema, "", format)
        return cinemas_showdates
