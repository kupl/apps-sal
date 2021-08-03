def save(sizes, hd):
    return save(sizes[:-1], hd) if sum(sizes) > hd else len(sizes)
