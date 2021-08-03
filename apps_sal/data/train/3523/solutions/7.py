def lenfilt(func, seq):
    return len(list(filter(func, seq)))


def assrt(seq):
    funcs = [str.isupper, str.islower, str.isdigit, str]
    nums = [0, 0, 0, 7]
    return [lenfilt(i, seq) > j for i, j in zip(funcs, nums)]


def password(string):
    return all(assrt(string))
