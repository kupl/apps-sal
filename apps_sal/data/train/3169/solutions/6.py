from collections import deque


def count_odd_pentaFib(n):
    if n == 0:
        return 0
    elif n < 6:
        return 1

    def pentabonacci(max_term):
        terms = deque((1, 1, 2, 4, 8), 5)
        m = max_term - 5
        for i in range(m):
            next_term = sum(terms)
            yield next_term
            terms.append(next_term)
    return len(set((term for term in pentabonacci(n) if term % 2 == 1))) + 1
