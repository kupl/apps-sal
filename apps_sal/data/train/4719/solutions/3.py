def sort_array(a):
    (sorted_odd, sorted_even) = (sorted((value for value in a if value & 1)), sorted([value for value in a if not value & 1], reverse=True))
    return [sorted_odd.pop(0) if value & 1 else sorted_even.pop(0) for value in a]
