for t in range(int(input())):
    n, k = map(int, input().split())
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    k = 100 - k
    f = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (l2[i] == 0 and l2[j] == 1) or (l2[i] == 1 and l2[j] == 0):
                if l1[i] + l1[j] <= k:
                    f = 1
                    break
            if f == 1:
                break
        if f == 1:
            break
    if f == 0:
        print("no")
    else:
        print("yes")
