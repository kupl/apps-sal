def game(a, b):
    if min(a, b) < 1:
        return "Non-drinkers can't play"
    i = 1
    while True:
        a -= i
        i += 1
        b -= i
        i += 1
        if min(a, b) < 0:
            return ["Mike", "Joe"][a < 0]
