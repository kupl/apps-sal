for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    i = 0
    temp = 0
    while i < n - 1:
        count = 1
        while i < n - 1 and (a[i + 1] < 0 and a[i] > 0 or (a[i + 1] > 0 and a[i] < 0)):
            count += 1
            i += 1
        while count > 0:
            print(count, end=' ')
            temp += 1
            count -= 1
        i += 1
    if temp != n:
        print(1)
    else:
        print('')
