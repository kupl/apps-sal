def remove_smallest(numbers):
    if numbers:
        out = numbers.copy()
        out.remove(min(out))
        return out
    else:
        return []
