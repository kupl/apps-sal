def sort_by_height(a):
    people = iter(sorted(n for n in a if n != -1))
    return [next(people) if n != -1 else n for n in a]
