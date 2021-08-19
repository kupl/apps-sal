from datetime import datetime


def get_zodiac_sign(day, month):
    date = datetime(1 + (month == 1 and day < 20), month, day)
    dates = [(20, 18), (19, 20), (21, 19), (20, 20), (21, 20), (21, 22), (23, 22), (23, 22), (23, 22), (23, 21), (22, 21), (22, 19)]
    signs = 'Aquarius Pisces Aries Taurus Gemini Cancer Leo Virgo Libra Scorpio Sagittarius Capricorn'.split()
    return next((s for (i, (d, s)) in enumerate(zip(dates, signs)) if datetime(1, i + 1, d[0]) <= date <= datetime(1 + (i == 11), (i + 1) % 12 + 1, d[1])))
