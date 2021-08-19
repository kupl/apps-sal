def number(lines):
    # If lines is empty, return empty
    if len(lines) == 0:
        return []

    # If not empty, return enumeration into string formatting
    return ["{}: {}".format(i + 1, item) for i, item in enumerate(lines)]
