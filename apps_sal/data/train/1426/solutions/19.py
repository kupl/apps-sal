t = int(input())
for i in range(t):
    (n, m) = [int(x) for x in input().split()]
    arr = []
    amt = [int(x) for x in input().split()]
    cost = 0
    brr = [0 for i in range(n)]
    for j in range(n):
        arr.append([int(y) for y in input().split()])
        if amt[arr[j][0] - 1] > 0:
            amt[arr[j][0] - 1] -= 1
            cost += arr[j][1]
            brr[j] = arr[j][0]
    r = 0
    for j in range(n):
        if brr[j] == 0:
            for k in range(r, m):
                if amt[k] > 0:
                    r = k
                    amt[k] -= 1
                    cost += arr[j][2]
                    brr[j] = k + 1
                    break
    print(cost)
    for j in range(n - 1):
        print(brr[j], end=' ')
    print(brr[-1])
