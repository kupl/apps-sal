for t in range(int(input())):
    (n, k) = map(int, input().split())
    numberlist = list(map(int, input().split()))
    result = ''
    for x in numberlist:
        if x % k == 0:
            result = result + '1'
        else:
            result = result + '0'
    print(result)
