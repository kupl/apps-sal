def max_number(n):
    s = str(n)
    temp = []

    for c in s:
        temp.append(c)

    temp.sort(reverse=True)
    s = ""
    for t in temp:
        s += t
    print(s)
    return int(s)
