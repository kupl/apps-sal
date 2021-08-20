def is_harshad(x):
    return not x % sum(map(int, [*str(x)]))


li = [*list(range(1, 10))]
l = []
for i in range(15):
    li = [x * 10 + i for x in li for i in range(10) if is_harshad(x * 10 + i)]
    l.extend(li)
l.append(10 ** 16)


def rthn_between(a, b):
    return [x for x in l if a <= x <= b]
