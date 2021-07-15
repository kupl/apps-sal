t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    sumA = sum(a)
    TWins = False
    for elem in a:
        if elem > sumA // 2:
            TWins = True
            break
    if TWins or sumA % 2 != 0:
        print("T")
    else:
        print("HL")
