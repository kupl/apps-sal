def calc(a):
    print(a)

    for i in range(len(a)):
        if a[i] > 0:
            a[i] *= a[i]

    for i in range(2, len(a), 3):
        a[i] *= 3

    for i in range(4, len(a), 5):
        a[i] *= -1

    return sum(a)
