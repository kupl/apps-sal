def balanced_num(number):
    n = str(number)
    a, b = 0, 0
    if len(n) <= 2:
        return 'Balanced'
    if len(n) % 2 == 0:
        for i in range(len(n) // 2 - 1):
            a += int(n[i])
        for j in range(len(n) // 2 + 1, len(n)):
            b += int(n[j])
        if a == b:
            return 'Balanced'
    else:
        for i in range(len(n) // 2):
            a += int(n[i])
        for j in range(len(n) // 2 + 1, len(n)):
            b += int(n[j])
        if a == b:
            return 'Balanced'
    return 'Not Balanced'
