from itertools import combinations_with_replacement


def find_prime(n):
    return all((n % i for i in range(2, int(n ** 0.5) + 1))) and n > 1


def solve(s, e):
    return len([1 for i in combinations_with_replacement([i for i in range(s, e) if find_prime(i)], 2) if find_prime(sum(map(int, str(i[0] * i[1]))))])
