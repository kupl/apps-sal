t = int(input())
for i in range(t):
    l = list(map(int, input().split()))
    n = l[0]
    k = l[1]
    m = list(map(int, input().split()))
    print(abs((max(m) + k) - (min(m) - k)))
