t = int(input())
for _ in range(t):
    n = int(input())
    list1 = list(map(int, input().strip().split()))
    x = max(list1)
    map1 = dict()
    for val in list1:
        if val in map1:
            map1[val] += 1
        else:
            map1[val] = 1
    ans = 1
    for val in map1:
        if val == x:
            if map1[val] > 1:
                ans = 0
                break
        elif map1[val] > 2:
            ans = 0
            break
    if ans:
        print('YES')
        ans1 = sorted(map1)
        ans2 = []
        for val in ans1:
            if map1[val] == 2:
                ans2.append(val)
        ans2.reverse()
        for val in ans1:
            print(val, end=' ')
        for val in ans2:
            print(val, end=' ')
        print()
    else:
        print('NO')
