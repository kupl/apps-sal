def string_suffix(str_):
    return sum(next((j for j, (a, b) in enumerate(zip(str_[i:], str_)) if a != b), len(str_) - i) for i in range(len(str_)))
