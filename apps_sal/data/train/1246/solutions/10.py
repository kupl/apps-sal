T = int(input())
while T > 0:
    T -= 1
    n = int(input())
    listA = list(map(int, input().split()))
    listB = list(map(int, input().split()))
    maxA = max(listA)
    maxB = max(listB)
    if maxB > maxA or maxA > maxB:
        print('YES')
    else:
        print('NO')
