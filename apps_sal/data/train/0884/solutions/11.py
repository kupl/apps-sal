t = int(input())

for i in range(t):
    s = input().split()
    x = int(s[0])
    k = int(s[1])
    factor_x = list()
    factor_k = list()
    for i in range(2, max(x, k) + 1):
        if(x % i == 0):
            factor_x.append(i)
        if(k % i == 0):
            factor_k.append(i)
    res_a = 0
    for i in factor_x:
        res_a += (i**k)
    res_b = 0
    for j in factor_k:
        res_b += (j * x)
    print(res_a, res_b)
