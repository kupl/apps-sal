from datetime import datetime


def to12hourtime(ts): return str(datetime.strptime(ts, '%H%M').strftime("%-I:%M %p").lower())
