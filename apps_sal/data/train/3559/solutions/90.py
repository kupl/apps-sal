def chromosome_check(sperm):
    x = 0
    y = 0
    for i in sperm:
        if i == "X":
            x += 1
        else:
            y += 1
    if x == 1 and y == 1:
        a = '''Congratulations! You\'re going to have a son.'''
        return a
    else:
        a = '''Congratulations! You\'re going to have a daughter.'''
        return a
