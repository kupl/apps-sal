def step_through_with(s):
    return any(m == n for m, n in zip(s, s[1:]))
