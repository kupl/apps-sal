def per(n):
    arr = []
    while n>9:
        s = 1
        for i in str(n):
            s *= int(i)
        n = s
        arr.append(n)
    return arr
