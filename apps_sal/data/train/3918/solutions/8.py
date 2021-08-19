def baby_count(x):
    x = x.lower()
    babies = 0
    letters = [x.count('b'), x.count('a'), x.count('y')]
    while min(letters) > 0 and letters[0] > 1:
        letters[0] -= 2
        letters[1] -= 1
        letters[2] -= 1
        babies += 1
    if babies == 0:
        return "Where's the baby?!"
    else:
        return babies
