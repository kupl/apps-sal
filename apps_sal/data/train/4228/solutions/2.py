def pal(s):
    return all((a == b for (a, b) in zip(s[:len(s) // 2], s[::-1])))


def palindrome(num):
    if type(123) != type(num):
        return 'Not valid'
    n = str(num)
    if any((not c.isdigit() for c in n)):
        return 'Not valid'
    (c, l) = (0, len(n))
    for i in range(2, l + 1):
        for j in range(l - i + 1):
            c += pal(n[j:j + i])
    return c
