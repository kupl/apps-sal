n = int(input())
while n > 0:
    line1 = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    ac = len(set(arr))
    ln = line1[0]
    k = line1[1]
    i = 0
    j = k - 1
    maxi = -1
    while(j < ln):
        if len(set(arr[i:j + 1])) == ac:
            maxi = max(maxi, sum(arr[i:j + 1]))
        i += 1
        j += 1
    print(maxi)
    n -= 1
