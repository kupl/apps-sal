# cook your dish here
n, a = map(int, input().split())
for i in range(a):
    if n != 0:
        r = n % 10
        n = n // 10
        if r != 0:
            r -= 1
            n = n * 10 + r
print(int(n))
