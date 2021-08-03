t = int(input())
for i in range(t):
    p1, p2, k = list(map(int, input().split()))
    p = 0
    p = p1 + p2
    d = 0
    d = p // k
    if(d % 2 == 0):
        print("CHEF")
    else:
        print("COOK")
