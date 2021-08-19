def shorten_to_date(long_date: str) -> str:
    return long_date.split(',', maxsplit=1)[0]
