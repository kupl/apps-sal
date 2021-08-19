t = int(input())
for i in range(t):
    a = input().split()
    k = int(a[0])
    n = int(a[1])
    maxlim = n - n % k
    no = maxlim / k
    ans = (k + maxlim) * no / 2
    if n % k != 0:
        print(int(ans))
    else:
        print(int(ans - n))
