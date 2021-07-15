def decode_resistor_colors(bands):
    color = {"black" : 0, "brown" : 1, "red" : 2, "orange" : 3, "yellow" : 4, "green" : 5, "blue" : 6, "violet" : 7, "gray" : 8, "white" : 9}
    tolerance = {"gold" : 5, "silver" : 10, "none" : 20}
    a, b, p, t, *_ = bands.split() + ["none"]
    c = (10 * color[a] + color[b]) * 10 ** color[p]
    r, m = next((c / x, y) for x, y in [(10 ** 6, "M"), (10 ** 3, "k"), (1, "")] if c // x > 0)
    return "{:g}{} ohms, {}%".format(r, m, tolerance[t])

