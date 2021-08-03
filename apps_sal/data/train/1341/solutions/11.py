t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split(' ')))
    start = -1
    for i in range(len(a) - 1):
        if a[i] >= a[i + 1]:
            start = i
            break
    end = -1
    for i in range(len(a) - 1, 0, -1):
        if a[i] <= a[i - 1]:
            end = i
            break
    # print(start,end)
    if start == -1:
        ans = ((n * (n + 1)) // 2) - 1
        print(ans)
    else:
        j = len(a) - 1
        k = 0
        c = 1
        for i in range(start, -1, -1):
            while a[j] > a[i] and j >= end:
                j -= 1
                c += 1
            k += c
            # print(k)
        k += len(a) - end
        print(k)
        # print(k+2)
