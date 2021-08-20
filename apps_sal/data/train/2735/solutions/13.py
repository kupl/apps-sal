def jumping_number(n):
    return ['Not!!', 'Jumping!!'][all((abs(ord(a) - ord(b)) == 1 for (a, b) in zip(str(n), str(n)[1:])))]
