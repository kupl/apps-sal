def to24hourtime(hour, minute, period):
    if hour == 12 and period == "am":
        hour = 0
    else: 
        hour += 12 if period == "pm" and hour != 12 else 0
    return f"{str(hour).rjust(2, '0')}{str(minute).rjust(2, '0')}"

