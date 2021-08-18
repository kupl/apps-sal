t = int(input())
for test in range(t):
    n = int(input())
    mydict = {}
    arr = list(map(int, input().strip().split()))
    minimum = 9999999
    for i in range(1, 9):
        mydict[i] = arr.count(i)
        if mydict[i] < minimum:
            minimum = mydict[i]
    print(minimum)
