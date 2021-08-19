def jumbled_string(s, n):
    a = s
    i = 0
    while i < n:            # Find the period of string after which it's the same
        s = s[::2] + s[1::2]
        i += 1
        if s == a:
            break
    n = n % i
    for i in range(n):
        s = s[::2] + s[1::2]
    return s
