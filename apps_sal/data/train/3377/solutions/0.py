def solve(time):
    def number(n):
        if n > 20: return "twenty {}".format(number(n - 20))
        return [
            None, "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine",
            "ten", "eleven", "twelve", "thirteen",
            "fourteen", "fifteen", "sixteen", "seventeen",
            "eighteen", "nineteen", "twenty"][n]
    hours, minutes = (int(s) for s in time.split(':'))
    if minutes <= 30:
        direction = "past"
    else:
        hours = (hours + 1) % 24
        direction = "to"
        minutes = 60 - minutes
    hour = number((hours + 11) % 12 + 1) if hours else "midnight"
    if minutes == 0:
        return "{} o'clock".format(hour) if hours else hour
    if minutes == 15:
        return "quarter {} {}".format(direction, hour)
    if minutes == 30:
        return "half past {}".format(hour)
    return "{} minute{} {} {}".format(
        number(minutes), "" if minutes == 1 else "s", direction, hour)

