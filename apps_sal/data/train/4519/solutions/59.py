def max_number(n):
    k = []
    s = ''
    for i in str(n):
        k.append(i)
        k.sort(reverse=True)
    for i in k:
        s += i
    return int(s)
