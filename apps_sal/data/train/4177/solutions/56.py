def men_from_boys(A):
    return sorted((e for e in set(A) if not e % 2)) + sorted((e for e in set(A) if e % 2), reverse=True)
