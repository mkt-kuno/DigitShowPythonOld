# !/usr/bin/python3
import enum


class Define:
    VERSION = "v0.0.0.1"
    MAX_CH = 16


class Result(enum.Enum):
    ID_OK       = 0
    ID_CANCEL   = 1000
    ID_CLOSE    = 1001
    ID_ERR      = 9000
