(an, jh) = ([1], [0])
for i in range(1, int(100000.0 * 5)):
    jh.append(i - an[jh[-1]])
    an.append(i - jh[an[-1]])


def john(n):
    return jh[:n]


def ann(n):
    return an[:n]


def sum_john(n):
    return sum(jh[:n])


def sum_ann(n):
    return sum(an[:n])
