t = int(input())
while(t > 0):
    n, k, e, m = map(int, input().split())
    scores = []
    for i in range(n - 1):
        sc = [int(x) for x in input().split()]
        scores.append(sum(sc))
    ram = [int(x) for x in input().split()]
    r = sum(ram)
    scores.sort(reverse=True)
    v = scores[k - 1]
    reqd = v - r + 1
    if(reqd < 0):
        print("0")
    elif(reqd > m):
        print("Impossible")
    else:
        print(reqd)
    t -= 1
