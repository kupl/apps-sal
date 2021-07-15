def find_digit(num, nth):
    if (nth <= 0):
        return -1
    num = abs(num)
    a = []
    while(num!=0):
        a.append(num%(10))
        num = num//10
    if nth >len(a):
        return 0
    else:
        return a[nth-1]
