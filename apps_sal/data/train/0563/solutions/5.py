ncases = int(input())
for cases in range(ncases):
    islands = int(input())
    pricelist = list(map(int, input().split()))
    if len(pricelist) != islands:
        continue
    visits = int(input())
    for k in range(visits):
        step = list(map(int, input().split()))
        print(sum(pricelist[step[0] - 1:step[1]]))
