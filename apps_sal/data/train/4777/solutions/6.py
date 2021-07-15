def string_from_range(x, y):
    while True:
        yield ''.join(sorted(list(''.join((str(i) for i in range(x, y))))))
        x += 1
        y += 1


def mystery_range(s, n):
    string = ''.join(sorted(list(s)))
    start = 0
    gen = string_from_range(start, start + n)
    for _ in range(10):
        if string == next(gen):
            return [start, start + n - 1]
        start += 1

    if len(s) % n == 0:
        begin, lenth, temp_list = 0, len(s) // n, []
        for _ in range(n):
            temp_list.append(int(s[begin:begin + lenth]))
            begin += lenth
        temp_list.sort()
        return [temp_list[0], temp_list[-1]]

    for _ in range(100):
        if string == next(gen):
            return [start, start + n - 1]
        start += 1

