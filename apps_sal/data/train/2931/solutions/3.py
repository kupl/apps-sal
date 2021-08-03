solution = __import__("functools").lru_cache(maxsize=None)(lambda n: 1 if n < 3 else solution(n - 1) + solution(n - 3))


def count_cows(n):
    if type(n) == int:
        return solution(n)
