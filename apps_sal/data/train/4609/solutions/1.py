def egged(year, span, chickens=3):
    production = [300, 240, 192, 153, 122, 97, 77, 61, 48, 38, 30, 24, 19, 15, 12, 9, 7, 5, 4, 3, 2, 1]
    return 'No chickens yet!' if not year else sum(production[:min(year, span)]) * chickens
