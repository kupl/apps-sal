eviternity = [int(n) for n in map(str, range(10 ** 6)) if set(n) <= set('358') and n.count('3') <= n.count('5') <= n.count('8')]
solve = lambda a, b, f=__import__('bisect').bisect_left: f(eviternity, b) - f(eviternity, a)
