from re import match as m


def date_checker(date):
    return m('(3[0-1]|[0-2]?\\d)-([0-1]?\\d)-\\d{4} [0-2]\\d:\\d\\d', date) != None
