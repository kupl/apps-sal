TRANSLATE = {0: "midnight", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
             7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve",
             13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
             19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty"}


def solve(time):
    def hourRepr(hour):
        return TRANSLATE[hour if hour <= 12 else hour % 12]

    def minuteRepr(minute, toNextHour=False):
        relative_minute = minute if not toNextHour else 60 - minute

        def repr(minute):
            if minute < 20 or minute % 10 == 0:
                return TRANSLATE[minute]
            return f"{TRANSLATE[minute // 10 * 10]} {TRANSLATE[minute % 10]}"
        return f"{repr(relative_minute)} minute{'s' if relative_minute > 1 else ''}"
    hour, minute = [int(t) for t in time.split(":")]
    if minute == 0:
        return f"{hourRepr(hour)} o'clock" if hour != 0 else hourRepr(hour)
    elif minute == 30:
        return f"half past {hourRepr(hour)}"
    elif minute % 15 == 0:
        return f"quarter past {hourRepr(hour)}" if minute == 15 else f"quarter to {hourRepr(hour + 1)}"
    else:
        return f"{minuteRepr(minute)} past {hourRepr(hour)}" if minute < 30 else f"{minuteRepr(minute, toNextHour=True)} to {hourRepr(hour + 1)}"
