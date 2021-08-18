for _ in range(int(input())):
    n, k = map(int, input().split())
    sum = 0
    maxi = n - k + 1
    if k > n:
        sum = 0
    else:
        for i in range(1, n + 1):
            sum += i
            if i == maxi:
                break
    print('Case' + ' ' + str(_ + 1) + ':', sum)
