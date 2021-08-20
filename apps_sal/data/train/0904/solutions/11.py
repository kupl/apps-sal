t = int(input())
for _ in range(t):
    (n, x) = map(int, input().split())
    l = list(map(int, input().split()))
    time = (n + 1) // 2
    (energy, flag) = (0, 1)
    temp = []
    for i in range(time):
        elem = max(l[0], l[-1])
        energy += elem
        if len(l) > 1:
            minn = min(l[0], l[-1])
            temp.append(elem)
            val = min(temp)
            if val < minn:
                energy = energy - val + minn
                temp.remove(val)
                temp.append(minn)
        l.pop(0)
        if l:
            l.pop()
        if energy >= x:
            print('YES')
            flag = 0
            break
    if flag:
        print('NO')
