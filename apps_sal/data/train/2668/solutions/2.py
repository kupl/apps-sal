def step_through_with(s):
    prev = ''
    for letter in s:
        if prev == letter:
            return True
        prev = letter
    return False
