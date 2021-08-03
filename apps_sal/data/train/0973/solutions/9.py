# cook your dish here
try:
    for _ in range(int(input())):
        n, k = map(int, input().split())
        li = list(map(int, input().split()))
        a = max(li)
        b = min(li)
        c = a + k
        d = b - k
        print(c - d)
except:
    pass
