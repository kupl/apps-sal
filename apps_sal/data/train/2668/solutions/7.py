def step_through_with(s):
    return any(s[i - 1] == x for i, x in enumerate(s[1:], 1))
