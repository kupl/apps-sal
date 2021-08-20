john_dict = {}
ann_dict = {}


def john_val(n):
    if n == 0:
        return 0
    if not n in john_dict:
        john_dict[n] = n - ann_val(john_val(n - 1))
    return john_dict[n]


def ann_val(n):
    if n == 0:
        return 1
    if not n in ann_dict:
        ann_dict[n] = n - john_val(ann_val(n - 1))
    return ann_dict[n]


def john(n):
    return [john_val(i) for i in range(n)]


def ann(n):
    return [ann_val(i) for i in range(n)]


def sum_john(n):
    return sum(john(n))


def sum_ann(n):
    return sum(ann(n))
