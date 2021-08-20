def sc(width, length, gaps):
    places = width * 2 + (length - 2) * 2
    if gaps == 0:
        return places
    (div, mod) = divmod(places, gaps + 1)
    if mod:
        return 0
    return div
