t = int(input())

for i in range(t):
    arr = input()
    l = list(map(int, arr.split(' ')))
    n = l[0]
    k = l[1]
    f = []
    f.append(k)
    f.append(k * (k - 1))
    if(n == 2):
        print(f[0] % 1000000007)
    if(n == 3):
        print(f[-1] % 1000000007)
    if(n > 3):
        for j in range(n - 3):
            f.append((f[-2] * k) + ((k - 1) * f[-1]))
            # print(f)
        print(f[-1] % 1000000007)
