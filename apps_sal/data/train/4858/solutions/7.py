(jm, am) = ({0: 0}, {0: 1})


def j(n):
    if n in jm.keys():
        return jm[n]
    jm[n] = n - a(j(n - 1))
    return jm[n]


def a(n):
    if n in am.keys():
        return am[n]
    am[n] = n - j(a(n - 1))
    return am[n]


def john(n):
    return [j(i) for i in range(n)]


def ann(n):
    return [a(i) for i in range(n)]


def sum_john(n):
    return sum(john(n))


def sum_ann(n):
    return sum(ann(n))
