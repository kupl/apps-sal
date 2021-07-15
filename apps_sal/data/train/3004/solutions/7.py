def head_smash(a):
    if type(a) == int: return "This isn't the gym!!"
    if not a: return "Gym is empty"
    return [s.replace('O',' ') for s in a]
