def current(usefulness):
    return sum(usefulness)


def needed(months):
    if months == 0:
        return 100
    else:
        return 0.85 * needed(months - 1)


def match(usefulness, months):
    if current(usefulness) < needed(months):
        return "No match!"
    else:
        return "Match!"
