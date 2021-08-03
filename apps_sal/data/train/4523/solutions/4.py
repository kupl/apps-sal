def solve(n): return max([n] + [n - n % 10**i - 1 for i in range(len(str(n)))], key=lambda n: (sum(map(int, str(n))), n))
