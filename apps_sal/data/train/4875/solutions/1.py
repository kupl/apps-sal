import re


def is_valid_coordinates(coordinates):
    return bool(re.match('-?(\\d|[1-8]\\d|90)\\.?\\d*, -?(\\d|[1-9]\\d|1[0-7]\\d|180)\\.?\\d*$', coordinates))
