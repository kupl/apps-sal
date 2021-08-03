def what_century(year):
    y = int(year)
    c, r = divmod(y, 100)
    if r:
        c += 1
    ones = c % 10
    tens = (c // 10) % 10
    if tens == 1:
        suffix = "th"
    elif ones == 1:
        suffix = "st"
    elif ones == 2:
        suffix = "nd"
    elif ones == 3:
        suffix = "rd"
    else:
        suffix = "th"
    return str(c) + suffix
