def step_through_with(s):
    return any((c1 == c2 for (c1, c2) in zip(s, s[1:])))
