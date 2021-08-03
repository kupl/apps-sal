def add(s1, s2):
    def char_sum(x): return sum(map(ord, x))
    return char_sum(s1) + char_sum(s2)
