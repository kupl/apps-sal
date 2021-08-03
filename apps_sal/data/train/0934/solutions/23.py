# cook your dish here
t = int(input())
for p in range(t):
    x, y, z = map(int, input().split())
    l = list(map(int, input().split()))
    m = list(map(int, input().split()))
    n = list(map(int, input().split()))
    s = 0
    for i in l:
        for j in m:
            for k in n:
                if i <= j and j >= k:
                    s = s + (((i + j) * (j + k)) % 1000000007)
    print(s % 1000000007)
