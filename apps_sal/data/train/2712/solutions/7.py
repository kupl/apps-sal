def left(num, n, i):
    s = 0
    counter = 0
    index = i - 1
    while index >= 0 and counter < n:
        s += int(num[index])
        index -= 1
        counter += 1
    return s


def right(num, n, i):
    s = 0
    counter = n
    index = i + 1
    while index < len(num) and counter:
        s += int(num[index])
        index += 1
        counter -= 1
    return s


def _sum(num, n, i):
    return left(num, n, i) + right(num, n, i)


def compare(one, others):
    for other in others:
        if one > other:
            return False
    return True


def check(ones, others):
    for one in ones:
        yield compare(one, others)


def loneliest(number):
    num = str(number)
    if not '1' in num:
        return False
    ones = []
    others = []
    for i in range(len(num)):
        s = _sum(num, int(num[i]), i)
        print()
        if num[i] == '1':
            ones.append(s)
        else:
            others.append(s)

    return any(list(check(ones, others)))
