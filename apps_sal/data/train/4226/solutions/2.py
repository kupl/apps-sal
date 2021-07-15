def remove_smallest(n):
    return n[:n.index(min(n))] + n[n.index(min(n)) + 1:] if n != [] else []
