def check(x, y, count):
    if x == y:
        print(count)


for i in range(int(input())):
    count = 0
    (x, y) = list(map(int, input().split()))
    diff = x - y
    if diff > 0:
        if diff % 2 == 0:
            x = x - diff
            count += 1
            check(x, y, count)
        else:
            x = x - (diff + 1)
            count += 1
            x = x + 1
            count += 1
            check(x, y, count)
    elif diff == 0:
        print('0')
    else:
        diff = abs(diff)
        if diff % 2 != 0:
            x = x + diff
            count += 1
            check(x, y, count)
        elif diff % 4 == 0:
            x = x + (diff + 1)
            count += 1
            x = x - (diff + 2)
            count += 1
            x = x + (diff + 1)
            count += 1
            check(x, y, count)
        else:
            a = diff / 2
            x = x + a
            count += 1
            x = x + a
            count += 1
            check(x, y, count)
