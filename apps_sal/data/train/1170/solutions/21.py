T = int(input())
for _ in range(T):
    n, k = list(map(int, input().split()))
    li = list(map(int, input().split()))[:n]
    s = ""
    for i in range(n):
        if(li[i] % k == 0):
            s = s + '1'
        else:
            s = s + '0'
    print(s)
