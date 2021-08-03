t = int(input())
for i in range(0, t):
    l, k = map(int, input().split())
    if(l < k):
        print("Case " + str(i + 1) + ":", "0")
    else:
        m = l - k + 1
        m = m * (m + 1) // 2
        print("Case " + str(i + 1) + ":", m)
