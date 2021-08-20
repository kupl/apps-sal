for i in range(int(input())):
    (r, c) = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    (maxx, minn) = (max(lst), min(lst))
    if maxx - minn < c:
        print('YES')
    else:
        print('NO')
