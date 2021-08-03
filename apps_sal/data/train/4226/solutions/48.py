def remove_smallest(n):
    if n:
        min_index = n.index(min(n))
        return n[:min_index] + n[min_index + 1:]
    else:
        return []
