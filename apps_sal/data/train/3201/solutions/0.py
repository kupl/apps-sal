import re

_24H = re.compile(r'^([01]?\d|2[0-3]):[0-5]\d$')

validate_time = lambda time: bool(_24H.match(time))

