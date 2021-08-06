def turn(n):
    if n % 9 == 0:
        return 9
    else:
        return (n % 9)


t = eval(input())
while t > 0:
    a, d, l, r = list(map(int, input().split()))
    diff = turn(d)
    s = 0
    box = []
    box.append(0)
    for i in range(1, 10):
        box.insert(i, turn(a))
        a = a + diff

    for i in range(l, r + 1):
        index = turn(i)
        s += box[index]

    print(s)
    t = t - 1
