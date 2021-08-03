def check_for_factor(base, factor):
    return [False, True][base % factor == 0]
