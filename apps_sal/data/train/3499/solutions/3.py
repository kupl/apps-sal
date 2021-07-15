def to24hourtime(hour, minute, period):
    return f"{period.startswith('p') * 12 + hour % 12:02d}{minute:02d}"


