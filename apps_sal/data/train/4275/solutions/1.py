def pattern(n):
    string = ''
    a = n
    if a % 2 == 0:
        a -= 1
    for x in range(1, a + 1):
        if x % 2 != 0:
            string += str(x) * x
            if x != a:
                string += '\n'
    return string
