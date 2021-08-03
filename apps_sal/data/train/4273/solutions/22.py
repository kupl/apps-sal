from re import match


def shorten_to_date(long_date: str) -> str:
    """ Get the shortened format of the given date (without time part). """
    return match("(?P<short_date>.+),", long_date).groupdict().get("short_date")
