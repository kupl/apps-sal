t = int(input())
for i in range(t):
    n, m, k = list(map(int, input().split()))
    d = abs(n - m)
    if k >= d:
        print("0")
    else:
        print((d - k))  # cook your dish here
