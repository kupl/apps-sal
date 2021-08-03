def rule30(list_, n):
    for _ in range(n):
        list_ = [0] + list_ + [0]
        list_ = [ruler(list_[i - 1], list_[i], list_[(i + 1) % len(list_)]) for i in range(len(list_))]
    return list_


def ruler(*args):
    data = [1 if x == 1 else 0 for x in args]
    x = int("".join(map(str, data)), 2)
    if x == 0 or x > 4:
        return 0
    else:
        return 1
