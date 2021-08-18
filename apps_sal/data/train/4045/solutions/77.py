def number(lines):
    if len(lines) == 0:
        return []

    return ["{}: {}".format(i + 1, item) for i, item in enumerate(lines)]
