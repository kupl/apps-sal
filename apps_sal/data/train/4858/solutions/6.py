def john_and_ann(n):
    john = [0]
    ann = [1]
    for i in range(1, n):
        (t1, t2) = (ann[i - 1], john[i - 1])
        john.append(i - ann[t2])
        ann.append(i - john[t1])
    return (john, ann)


def ann(n):
    (john, ann) = john_and_ann(n)
    return ann


def john(n):
    (john, ann) = john_and_ann(n)
    return john


def sum_ann(n):
    Ann = ann(n)
    return sum(Ann)


def sum_john(n):
    John = john(n)
    return sum(John)
