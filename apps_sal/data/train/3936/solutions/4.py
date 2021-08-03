def wrapper_fun(func, lst): return func(lst)
def fib(lst): return lst[-1] + lst[-2]
def tri(lst): return lst[-1] + lst[-2] + lst[-3]
def tet(lst): return lst[-1] + lst[-2] + lst[-3] + lst[-4]
def pad(lst): return lst[-2] + lst[-3]
def pel(lst): return lst[-1] * 2 + lst[-2]
def jac(lst): return lst[-1] + lst[-2] * 2


def zozonacci(pattern, length):
    if not pattern or not length:
        return []
    if length < 5:
        if pattern[0] == 'pad':
            return [0, 1, 0, 0][:length]
        else:
            return [0, 0, 0, 1][:length]
    cp_lst = zozonacci(pattern, length - 1)
    return cp_lst + [wrapper_fun(eval(pattern[(length - 5) % len(pattern)]), cp_lst)]
