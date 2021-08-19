# cook your dish here
for _ in range(int(input())):
    n, l, h = list(map(int, input().split()))
    print(n - l + 1 + 2**(l) - 2, 1 + 2**(h) - 2 + 2**(h - 1) * (n - h))
