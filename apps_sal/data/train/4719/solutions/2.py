def sort_array(a):
    odds = iter(sorted(n for n in a if n % 2))
    evens = iter(sorted((n for n in a if not n % 2), reverse=True))
    return [next(odds) if n % 2 else next(evens) for n in a]
