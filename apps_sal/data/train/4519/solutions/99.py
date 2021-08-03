def max_number(n):
    a = str(n)
    b = ''
    lst = []

    for ch in a:
        lst.append(ch)

    lst.sort(reverse=True)

    for x in lst:
        b += x

    return int(b)
