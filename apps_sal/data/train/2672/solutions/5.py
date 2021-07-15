def color_probability(color, texture):
    bag = [
        ("red", "smooth"),
        ("red", "bumpy"),
        ("red", "bumpy"),
        ("red", "bumpy"),
        ("red", "bumpy"),
        ("yellow", "bumpy"),
        ("yellow", "bumpy"),
        ("yellow", "smooth"),
        ("green", "bumpy"),
        ("green", "smooth"),
    ]
    candidates = [marble for marble in bag if marble[1] == texture]
    return "{:.03}".format(sum(marble[0] == color for marble in candidates) / len(candidates))[:-1]
