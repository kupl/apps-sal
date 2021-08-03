weight = lambda n, w, e=__import__('math').exp(-2): (1 - 3 * e) / (1 - e) / 4 * (1 - e**n) * w
