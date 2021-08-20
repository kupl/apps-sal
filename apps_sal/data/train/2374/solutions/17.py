Q = int(input())
for q in range(Q):
    n = int(input())
    arr1 = [int(i) for i in input()]
    arr2 = [int(i) for i in input()]
    error = False
    now_x = 0
    now_y = 0
    was_x = -1
    while now_x < n:
        if now_y == 0:
            now = arr1[now_x]
        else:
            now = arr2[now_x]
        if True:
            if now in {1, 2}:
                if was_x == now_x:
                    error = True
                    break
                else:
                    (was_x, now_x) = (now_x, now_x + 1)
            elif was_x == now_x:
                was_x = now_x
                now_x += 1
            else:
                was_x = now_x
                now_y = (now_y + 1) % 2
    if now_y == 0:
        error = True
    if error:
        print('NO')
    else:
        print('YES')
