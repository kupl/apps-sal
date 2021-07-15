def solve(a):
    b = [0] * len(a)
    c = 0
    for i in a:
        if i.isalpha():
            a = a.replace(i, " ")
    a = a.split()
    for x in range(len(a)):
        b[x] = int(a[x])
        c += 1
    return max(b)
