def jumping_number(number):
    n = list(map(int, str(number)))
    if len(str(number)) == 1:
        return 'Jumping!!'
    else:
        return ["Not!!", "Jumping!!"][False not in [abs(a - b) == 1 for a, b in zip(n, n[1:])]]
