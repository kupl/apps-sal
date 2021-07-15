def moment_of_time_in_space(moment):
    d = sum(int(c) if c in '123456789' else -1 for c in moment)
    return [d < 0, d == 0, d > 0]
