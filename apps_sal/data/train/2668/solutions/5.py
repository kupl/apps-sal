def step_through_with(s):
    return any(map(str.__eq__, s, s[1:]))
