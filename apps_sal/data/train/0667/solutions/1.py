t = int(input())
for _ in range(t):
    nd = list(map(int, input().split()))
    n = nd[0]
    d = nd[1]
    cutOff = []
    x = d
    buses = list(map(int, input().split()))
    for i in range(len(buses)-1,-1,-1):
        x = x - x%buses[i]
    print(x)











            


