def withdraw(n):
    (hundreds, fifties, rest) = (n // 100, n % 100 // 50, n % 50)
    if rest % 20 == 10:
        if fifties == 0:
            (hundreds, fifties, twenties) = (hundreds - 1, 1, (rest + 50) // 20)
        else:
            (fifties, twenties) = (fifties - 1, (rest + 50) // 20)
    else:
        twenties = rest // 20
    return [hundreds, fifties, twenties]
