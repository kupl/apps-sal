def prime(num):
    if n > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
                break
        else:
            return True
    else:
        return False


t = int(input())
for k in range(t):
    n = int(input())
    a = [0] * n
    l = list(map(int, input().split()))
    s = max(l)
    a1 = [0] * (s + 1)
    i = 2
    while i <= s:
        if prime(i):
            for j in range(i, s + 1, i):
                a1[j] = i
        i += 1
    for j in range(n):
        a[j] = a1[l[j]]
    a.sort()
    ti = 1
    ma = 1
    nu = a[0]
    for j in range(1, n):
        if a[j] == a[j - 1]:
            ti += 1
        else:
            if ti >= ma:
                ma = ti
                nu = a[j - 1]
            ti = 1
    if ti >= ma:
        ma = ti
        nu = a[n - 1]
    print(nu)
