def string_suffix(str_):
    return sum(next((c for c, (a, b) in enumerate(zip(str_, str_[d:])) if a != b), len(str_[d:])) for d in range(len(str_)))
