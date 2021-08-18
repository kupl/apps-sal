N = int(input())
for i in range(N):
    m, o, k = list(map(int, input().split()))
    d = abs(m - o)
    if(k > d):
        print(0)
    else:
        print(d - k)
