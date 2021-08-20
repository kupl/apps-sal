x = eval(input())
a = list(map(int, input().split()))
q = eval(input())
for __ in range(q):
    (l, r) = list(map(int, input().split()))
    l -= 1
    R = sorted(a[l:r])
    x = 0
    for ii in range(1, len(R)):
        x += (R[ii] - R[ii - 1]) ** 2
    print(x)
