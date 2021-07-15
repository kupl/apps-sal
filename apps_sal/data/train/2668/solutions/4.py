def step_through_with(s):
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if letter * 2 in s:
            return True
    return False
