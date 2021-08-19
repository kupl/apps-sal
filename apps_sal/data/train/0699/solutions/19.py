t = int(input())
for i in range(t):
    (n, k, d) = map(int, input().split())
    arr = list(map(int, input().split()))
    s = sum(arr)
    c = s // k
    if c >= d:
        print(d)
    else:
        print(c)
