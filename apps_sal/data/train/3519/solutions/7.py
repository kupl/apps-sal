def duplicate_elements(m, n):
    return len(m + n) != len(set(m + n))
