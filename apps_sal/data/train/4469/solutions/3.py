def is_narcissistic(n): return sum(int(i) ** len(str(n)) for i in str(n)) == n
