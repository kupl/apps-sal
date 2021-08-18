t = int(input())
for r in range(t):
    p1, p2, k = map(int, input().split())
    x = p1 + p2
    y = x // k
    if(y % 2 == 0):
        print("CHEF")
    else:
        print("COOK")
