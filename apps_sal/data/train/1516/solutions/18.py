# cook your dish here
t = int(input())
mod = 10**9 + 7
for i in range(t):
    n, k = input().split(' ')
    ki = int(k)
    ni = int(n)
    km = ki - 1
    nm = ni - 1
    q = km // nm
    r = km % nm
    # print(r,q)
    a = km + (q * r) + (nm * q * (q - 1)) // 2
    if ni == 2:
        a = (((ki) * (ki - 1)) // 2) % mod
    ans = a % mod
    print(ans)
    # print(r,q,a)
