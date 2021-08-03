t = triangle = lambda r: r[0]if len(r) == 1else t([a if a == b else(set("RGB") - {a, b}).pop()for a, b in zip(r, r[1:])])
