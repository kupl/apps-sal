def f1(n, k):
    n_i = n
    while True:
        if all((int(c) < k for c in str(n_i))):
            return n_i
        n_i += n


def f2(n, k):
    n_i = n
    while True:
        if set(str(n_i)) == set((str(d) for d in range(k))):
            return n_i
        n_i += n


def find_f1_eq_f2(n, k):
    n_i = n + 1
    while True:
        if f1(n_i, k) == f2(n_i, k):
            return n_i
        n_i += 1
