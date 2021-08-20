t = int(input())
while t > 0:
    n = int(input())
    s = str(input())
    A = list(map(int, input().split()))
    maxi = 0
    for i in range(0, n - 7):
        summ = 0
        new = ''
        k = 0
        for j in range(i, i + 8):
            if s[j] == 'D' or s[j] == 'T':
                new = new + s[j]
            if s[j] == 'd':
                summ += 2 * A[k]
            elif s[j] == 't':
                summ += 3 * A[k]
            else:
                summ += A[k]
            k += 1
        for x in new:
            if x == 'D':
                summ = 2 * summ
            else:
                summ = 3 * summ
        if summ > maxi:
            maxi = summ
    print(maxi)
    t = t - 1
