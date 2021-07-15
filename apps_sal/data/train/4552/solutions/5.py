rankings = lambda xs: list(map(dict(map(reversed, enumerate(sorted(xs, reverse=True), 1))).__getitem__, xs))
