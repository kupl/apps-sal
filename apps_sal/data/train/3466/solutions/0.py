from re import match


def date_checker(date):
    return bool(match(r'\d{2}-\d{2}-\d{4}\s\d{2}:\d{2}', date))

