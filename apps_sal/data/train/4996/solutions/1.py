def fibs_fizz_buzz(n):
    a, b, f = 1, 1, []
    for _ in range(n):
        s = ""
        if not a % 3:
            s += "Fizz"
        if not a % 5:
            s += "Buzz"
        f.append(s or a)
        a, b = b, a + b
    return f
