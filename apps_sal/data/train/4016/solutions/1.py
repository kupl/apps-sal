def game(a, b):
    if a * b:
        c = int(a ** 0.5)
        return ('Mike', 'Joe')[c * (c + 1) <= b]
    return "Non-drinkers can't play"
