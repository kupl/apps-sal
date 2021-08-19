t = int(input())
while t > 0:
    (a, b, c) = [int(x) for x in input().split()]
    _count = pos_max = 0
    _max = 100 * a + b
    while a * 100 + b > c and _count <= 10000:
        if b < c:
            a -= 1
            b += 100
        b -= c
        temp = b
        b = a
        a = temp
        _count += 1
        if a * 100 + b > _max:
            _max = a * 100 + b
            pos_max = _count
    print(pos_max)
    t -= 1
