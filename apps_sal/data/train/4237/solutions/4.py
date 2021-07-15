from datetime import datetime

to12hourtime = lambda ts: str(datetime.strptime(ts, '%H%M').strftime("%-I:%M %p").lower())
