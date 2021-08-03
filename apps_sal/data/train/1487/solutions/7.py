t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(y) for y in input().split()]
    x = int(input())
    ca = [0] * n
    cb = [0] * n
    psum, psumr, aeats, beats = 0, 0, 0, 0
    tie = False
    for i in range(n):
        psum = psum + a[i]
        psumr = psumr + a[n - i - 1]
        if i < n - 1:
            ca[i + 1] = psum / x
            cb[n - i - 2] = psumr

    for i in range(n):
        if cb[i] > ca[i]:
            aeats += 1
        elif cb[i] < ca[i]:
            beats += 1
        else:
            tie = True
    if (tie):
        if beats > aeats:
            beats += 1
        else:
            aeats += 1
    print("{} {}".format(aeats, beats))
