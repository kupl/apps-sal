t = int(input())
for i in range(t):
    n = int(input())
    ls = list(map(int, input().split()))
    s = len(set(ls))
    print(s)
