t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if n == 4:
        target = -1
        cur = -1
        ind = -1
        s = set()
        flag = False
        for i in range(1, n):
            k = a[i] - a[i - 1]
            if k not in s:
                s.add(k)
            else:
                target = k
                cur = a[i]
                ind = i
                flag = True
                break
        if flag:
            back = [cur]
            forth = [cur]
            for i in range(ind + 1, n):
                forth.append(forth[-1] + target)
            for i in range(ind - 1, -1, -1):
                back.append(back[-1] - target)
            back = back[::-1]
            back.pop()
            print(*back, end=' ')
            print(*forth)
        else:
            k = (a[-1] - a[0]) // (n - 1)
            for i in range(n - 1, -1, -1):
                print(a[-1] - k * i, end=' ')
            print()
    else:
        target = -1
        cur = -1
        ind = -1
        s = set()
        for i in range(1, n):
            k = a[i] - a[i - 1]
            if k not in s:
                s.add(k)
            else:
                target = k
                cur = a[i]
                ind = i
                break
        back = [cur]
        forth = [cur]
        for i in range(ind + 1, n):
            forth.append(forth[-1] + target)
        for i in range(ind - 1, -1, -1):
            back.append(back[-1] - target)
        back = back[::-1]
        back.pop()
        print(*back, end=' ')
        print(*forth)
