def next_bigger(n):
    if str(n) == ''.join(sorted(str(n))[::-1]):
        return -1
    a = n
    while True:
        a += 1
        if sorted(str(a)) == sorted(str(n)):
            return a
