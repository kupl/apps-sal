is_narcissistic = lambda n: sum(int(i) ** len(str(n)) for i in str(n)) == n
