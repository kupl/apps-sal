def super_size(n):
    x = list(str(n))
    z = []
    for k in x:
        z.append(int(k))
    z.sort()
    z = z[::-1]
    y = ''
    for k in z:
        y += str(k)
    y = int(y)
    return y

    # your code here
