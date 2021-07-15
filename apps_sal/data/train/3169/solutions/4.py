penta_fib_table = {
    0: 0,
    1: 1,
    2: 1,
    3: 2,
    4: 4
}
def penta_fib(n):
    if n in penta_fib_table:
        return penta_fib_table[n]
    return penta_fib(n - 1) + penta_fib(n - 2) + penta_fib(n - 3) + penta_fib(n - 4) + penta_fib(n - 5)

def count_odd_pentaFib(n):
    odd_terms = []
    for i in range(1, n + 1):
        penta_fib_i = penta_fib(i)
        penta_fib_table[i] = penta_fib_i
        if penta_fib_i % 2 == 1:
            odd_terms.append(penta_fib_i)
    return len(set(odd_terms))
