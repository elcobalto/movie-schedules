from movie_schedules.constants.cinemark import (
    CINEMA_ZONES_TAGS as CINEMARK_CINEMA_ZONES_TAGS,
)
from movie_schedules.constants.cinemark import CINEMAS_TAGS as CINEMARK_CINEMAS_TAGS
from movie_schedules.constants.cinepolis import (
    CINEMA_ZONES_TAGS as CINEHOYTS_CINEMA_ZONES_TAGS,
)
from movie_schedules.constants.cinepolis import CINEMAS_TAGS as CINEHOYTS_CINEMAS_TAGS

CINEMAS_ZONES = CINEHOYTS_CINEMA_ZONES_TAGS + CINEMARK_CINEMA_ZONES_TAGS
CINEMAS = CINEHOYTS_CINEMAS_TAGS + CINEMARK_CINEMAS_TAGS


TD_ESP = "2D ESP"
TD_SUB = "2D SUB"
ESP = "ESP"
SUB = "SUB"
