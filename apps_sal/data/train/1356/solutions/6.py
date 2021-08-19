ans = [1]


def bell_numbers(start, stop):
    if stop < start:
        (start, stop) = (stop, start)
    if start < 1:
        start = 1
    if stop < 1:
        stop = 1
    t = [[1]]
    c = 1
    while c <= stop:
        if c >= start:
            yield t[-1][0]
        row = [t[-1][-1]]
        for b in t[-1]:
            row.append((row[-1] % 1000000007 + b % 1000000007) % 1000000007)
        c += 1
        t.append(row)
        ans.append(row[-1])
    t = list(t)


b = []
b = bell_numbers(1, 1001)
x = eval(input())
count = 1
for i in b:
    count += 1
while x > 0:
    y = eval(input())
    print(ans[y - 1] % 1000000007)
    x = x - 1
