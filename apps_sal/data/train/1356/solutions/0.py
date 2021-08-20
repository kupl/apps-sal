t = [[1]]


def bell_numbers(start, stop):
    if stop < start:
        (start, stop) = (stop, start)
    if start < 1:
        start = 1
    if stop < 1:
        stop = 1
    c = 1
    while c <= stop:
        if c >= start:
            yield t[-1][0]
        row = [t[-1][-1]]
        for b in t[-1]:
            row.append((row[-1] + b) % 1000000007)
        c += 1
        t.append(row)


ar = [0] * 1001
i = 0
for b in bell_numbers(1, 1001):
    ar[i] = b
    i += 1
T = eval(input())
while T:
    N = eval(input())
    print(ar[N])
    T -= 1
