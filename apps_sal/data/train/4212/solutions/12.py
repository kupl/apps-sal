def unite_unique(*array):
    return [y for x, y in enumerate(sum(array, [])) if y not in sum(array, [])[:x]]
