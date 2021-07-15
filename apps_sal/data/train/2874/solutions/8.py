def my_parse_int(string):
    """Parses an str for an int value. If the str does not convert to a valid int, return the "NaN" string."""
    try:
        return int(string)
    except ValueError:
        return "NaN"
