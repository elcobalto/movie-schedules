from difflib import SequenceMatcher
from typing import List, Optional, Tuple

from movie_schedules.constants.main import CINEMAS, CINEMAS_ZONES
from movie_schedules.dataclasses.cinema import Cinema, ShowDate
from movie_schedules.services.cinemark import CinemarkService
from movie_schedules.services.cinepolis import CinepolisService


class CinemaBot:
    cinemark_service = CinemarkService()
    cinepolis_service = CinepolisService()

    def get_chain(self, cinema: str) -> Optional[str]:
        if self.cinepolis_service.is_chain(cinema):
            return "CINEHOYTS"
        elif self.cinemark_service.is_chain(cinema):
            return "CINEMARK"
        return None

    def get_showings(self, movie, date, cinema, format) -> ShowDate:
        chain = self.get_chain(cinema)
        if chain == "CINEHOYTS":
            return self.cinepolis_service.get_showings(movie, date, cinema, format)
        elif chain == "CINEMARK":
            return self.cinemark_service.get_showings(movie, date, cinema, format)

    def get_showings_by_zone(self, movie, date, cinema, format) -> ShowDate:
        cinehoyts_cinemas = self.cinepolis_service.get_showings_by_zone(
            movie, date, cinema, format
        )
        cinemark_cinemas = self.cinemark_service.get_showings_by_zone(
            movie, date, cinema, format
        )
        return ShowDate(date=date, cinemas=cinehoyts_cinemas + cinemark_cinemas)

    def get_showing_by_date(self, movie, date, format) -> ShowDate:
        cinehoyts_cinemas = self.cinepolis_service.get_showing_by_date(
            movie, date, format
        )
        cinemark_cinemas = self.cinemark_service.get_showing_by_date(
            movie, date, format
        )
        return ShowDate(date=date, cinemas=cinehoyts_cinemas + cinemark_cinemas)

    def get_general_showings(
        self, movie: str, date: str, cinema: str = None, format: str = None
    ) -> Tuple[str, int]:
        cinema_is_zone = cinema in CINEMAS_ZONES
        if cinema and not cinema_is_zone:
            cinema_showings = self.get_showings(movie, date, cinema, format)
            message, total = self.get_movie_date_message([cinema_showings], "CINEMA")
        elif cinema and cinema_is_zone:
            cinema_showings = self.get_showings_by_zone(movie, date, cinema, format)
            message, total = self.get_movie_date_message([cinema_showings], "CINEMA")
        else:
            cinema_showings = self.get_showing_by_date(movie, date, format)
            message, total = self.get_movie_date_message([cinema_showings], "CINEMA")
        return message, total

    def get_showing_by_cinema(
        self, movie: str, cinema: str, format: str
    ) -> List[ShowDate]:
        cinema_is_zone = cinema in CINEMAS_ZONES
        if not cinema_is_zone:
            chain = self.get_chain(cinema)
            if chain == "CINEHOYTS":
                return self.cinehoyts_services.get_showing_by_cinema(
                    movie, cinema, format
                )
            elif chain == "CINEMARK":
                return self.cinepolis_service.get_showing_by_cinema(
                    movie,
                    self.cinepolis_service.get_cinema_by_cinema_key(cinema),
                    format,
                )
            else:
                cinehoyts_showings = self.cinepolis_service.get_showing_by_cinema(
                    movie, cinema, format
                )
                cinemark_showings = self.cinemark_service.get_showing_by_cinema(
                    movie,
                    self.cinemark_service.get_cinema_by_cinema_key(cinema),
                    format,
                )
                return cinehoyts_showings + cinemark_showings
        else:
            cinehoyts_showings = self.cinepolis_service.get_showing_by_zone(
                movie, cinema, format
            )
            cinemark_showings = self.cinemark_service.get_showing_by_zone(
                movie, cinema, format
            )
            return cinehoyts_showings + s

    def get_cinema_showings_by_date(self, cinema, date, format) -> ShowDate:
        chain = self.get_chain(cinema)
        if chain == "CINEHOYTS":
            return self.cinepolis_service.get_cinema_showings_by_date(
                cinema, date, format
            )
        elif chain == "CINEMARK":
            return self.cinemark_service.get_cinema_showings_by_date(
                self.cinemark_service.get_cinema_by_cinema_key(cinema), date, format
            )

    def get_cinema_showings_by_date_and_zone(
        self, cinema, date, format
    ) -> List[ShowDate]:
        cinehoyts_showings = (
            self.cinepolis_service.get_cinema_showings_by_date_and_zone(
                cinema, date, format
            )
        )
        cinemark_showings = self.cinemark_service.get_cinema_showings_by_date_and_zone(
            cinema, date, format
        )
        return cinehoyts_showings + cinemark_showings

    def get_cinema_showings(self, cinema, format) -> List[ShowDate]:
        chain = self.get_chain(cinema)
        if chain == "CINEHOYTS":
            return self.cinepolis_service.get_cinema_showings(cinema, format)
        elif chain == "CINEMARK":
            return self.cinemark_service.get_cinema_showings(cinema, format)

    def get_cinema_showings_by_zone(self, cinema, format) -> List[ShowDate]:
        cinehoyts_showings = self.cinepolis_service.get_cinema_showings_by_zone(
            cinema, format
        )
        cinemark_showings = self.cinemark_service.get_cinema_showings_by_zone(
            cinema, format
        )
        return cinehoyts_showings + cinemark_showings

    def get_general_cinema_showings(
        self, cinema: str, date: str = None, format: str = None
    ) -> Tuple[str, int]:
        cinema_is_zone = cinema in CINEMAS_ZONES
        if not cinema_is_zone and date:
            cinema_showings = self.get_cinema_showings_by_date(cinema, date, format)
            message, total = self.get_movie_date_message([cinema_showings], "CINEMA")
        elif not cinema_is_zone and not date:
            cinema_showings = self.get_cinema_showings(cinema, format)
            message, total = self.get_movie_date_message(cinema_showings, "CINEMA")
        elif cinema_is_zone and date:
            cinema_showings = self.get_cinema_showings_by_date_and_zone(
                cinema, date, format
            )
            message, total = self.get_movie_date_message(cinema_showings, "CINEMA")
        else:
            cinema_showings = self.get_cinema_showings_by_zone(cinema, format)
            message, total = self.get_movie_date_message(cinema_showings, "CINEMA")
        return message, total

    def get_movie_date_message(
        self, showdates: List[ShowDate], separator_type: str
    ) -> Tuple[str, int]:
        result = ""
        total_shotimes = 0
        for showdate in showdates:
            if not showdate:
                continue
            temp_result = f"{showdate.get_formatted_date()}\n\n"
            is_there_any_cinema = False
            for cinema in showdate.cinemas:
                movie_temp_result = f"{cinema.name}\n\n"
                is_there_any_movie = False
                for movie in cinema.movies:
                    show_temp_result = f"{movie.get_formatted_title()}\n"
                    is_there_showtime = False
                    for showtime in movie.showtimes:
                        is_there_any_cinema = True
                        is_there_any_movie = True
                        is_there_showtime = True
                        if showtime.seats:
                            seats = (
                                f"{showtime.seats} asientos disponibles"
                                if int(showtime.seats) > 0
                                else "AGOTADA"
                            )
                            show_temp_result += f"{showtime.showtime} hrs — {showtime.format} — {seats}\n"
                        else:
                            show_temp_result += (
                                f"{showtime.showtime} hrs — {showtime.format}\n"
                            )
                        total_shotimes += 1
                    show_temp_result += "——————\n\n"
                    if separator_type == "MOVIE":
                        show_temp_result += "\n\n$SEPARATOR$"
                    if is_there_showtime:
                        movie_temp_result += show_temp_result
                if separator_type == "CINEMA":
                    movie_temp_result += "$SEPARATOR$"
                if is_there_any_movie:
                    temp_result += movie_temp_result
            if is_there_any_cinema:
                result += temp_result
            if separator_type == "SHOWTIME":
                result += "\n\n$SEPARATOR$"
        return result, total_shotimes

    def similar(self, a, b):
        return SequenceMatcher(None, a, b).ratio()

    def check_movie_in_total(self, movie_title, total):
        movie_title.replace("¡", "").replace("!", "").replace("¿", "").replace(
            "?", ""
        ).replace(",", "").replace(".", "").replace(":", "")
        for possible_movie in total.keys():
            possible_movie.replace("¡", "").replace("!", "").replace("¿", "").replace(
                "?", ""
            ).replace(",", "").replace(".", "").replace(":", "")
            similarity = self.similar(movie_title, possible_movie)
            minimum_title_len = min(len(movie_title), len(possible_movie))
            first_similarity = self.similar(
                movie_title[:minimum_title_len], possible_movie[:minimum_title_len]
            )
            last_similarity = self.similar(
                movie_title[-minimum_title_len:], possible_movie[-minimum_title_len:]
            )

            if (
                (len(movie_title) >= 5 and len(possible_movie) >= 5)
                and ((movie_title in possible_movie) or (possible_movie in movie_title))
            ) or (
                similarity > 0.66 or first_similarity > 0.85 or last_similarity > 0.85
            ):
                return True, possible_movie
        return False, movie_title

    def get_movie_total(self, cinemas: List[Cinema]) -> str:
        total = {}
        for cinema in cinemas:
            for movie in cinema.movies:
                movie_title = movie.title.upper().replace("-", " ").replace(":", "")
                movie_exists, movie_key = self.check_movie_in_total(movie_title, total)
                if movie_exists:
                    total[movie_key] += len(movie.showtimes)
                else:
                    total[movie_key] = len(movie.showtimes)
        total = {
            k: v
            for k, v in sorted(total.items(), key=lambda item: item[1], reverse=True)
        }
        message = ""
        for movie_title in total.keys():
            message += f"{movie_title}: {total[movie_title]}\n"
        return message

    def get_format_total(self, cinemas: List[Cinema]) -> str:
        total = {}
        for cinema in cinemas:
            for movie in cinema.movies:
                for showtime in movie.showtimes:
                    showtime_format = showtime.format
                    if showtime_format in total:
                        total[showtime_format] += 1
                    else:
                        total[showtime_format] = 1
        total = {
            k: v
            for k, v in sorted(total.items(), key=lambda item: item[1], reverse=True)
        }
        message = ""
        for showtime_format in total.keys():
            message += f"{showtime_format}: {total[showtime_format]}\n"
        return message

    def get_cinema_total(self, cinemas: List[Cinema]) -> str:
        total = {}
        for cinema in cinemas:
            for movie in cinema.movies:
                if cinema.name in total:
                    total[cinema.name] += len(movie.showtimes)
                else:
                    total[cinema.name] = len(movie.showtimes)
        total = {
            k: v
            for k, v in sorted(total.items(), key=lambda item: item[1], reverse=True)
        }
        message = ""
        for cinema_name in total.keys():
            message += f"{cinema_name}: {total[cinema_name]}\n"
        return message

    def get_total(self, date: str, format: str) -> str:
        cinehoyts_total = self.cinepolis_service.get_total(date, format)
        cinemark_total = self.cinemark_service.get_total(date, format)
        total = self.get_movie_total(cinehoyts_total + cinemark_total)
        return total

    def get_format_total(self, date: str, format: str) -> str:
        cinehoyts_total = self.cinepolis_service.get_total(date, format)
        cinemark_total = self.cinemark_service.get_total(date, format)
        total = self.get_format_total(cinehoyts_total + cinemark_total)
        return total

    def get_cinema_total(self, date: str, format: str) -> str:
        cinehoyts_total = self.cinepolis_service.get_total(date, format)
        cinemark_total = self.cinemark_service.get_total(date, format)
        total = self.get_cinema_total(cinehoyts_total + cinemark_total)
        return total

    def get_info_cities(self):
        info = ""
        uniques = {}
        CINEMAS_ZONES.sort()
        for cinema in CINEMAS_ZONES:
            if cinema in uniques:
                continue
            info += f"{cinema}\n"
            uniques[cinema] = True
        return info

    def get_info_cinemas(self):
        info = ""
        uniques = {}
        CINEMAS.sort()
        for cinema in CINEMAS:
            if cinema in uniques:
                continue
            info += f"{cinema}\n"
            uniques[cinema] = True
        return info
