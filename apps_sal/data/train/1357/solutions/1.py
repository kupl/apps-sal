for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    counter = [0, 0, 0]
    flag = False
    for i in arr:
        if i == 5:
            counter[0] += 1
        elif i == 10:
            counter[1] += 1
            counter[0] -= 1
        else:
            counter[2] += 1
            if counter[1] > 0:
                counter[1] -= 1
            else:
                counter[0] -= 2
        if counter[0] < 0 or counter[1] < 0:
            flag = True
    print('NO') if flag else print('YES')
