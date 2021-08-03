from bisect import bisect
F = [2, 4, 16, 37, 58, 89, 145, 42, 20]


def f(n):
    for i in range(50):
        n = sum(int(i)**2 for i in str(n))
        if n in F:
            return False
        if n == 1:
            return True


H = [i for i in range(1, 300000) if f(i)]


def performant_numbers(n):
    return H[:bisect(H, n)]
