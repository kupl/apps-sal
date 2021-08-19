def step_through_with(s):
    return any((l + l in s for l in s))
