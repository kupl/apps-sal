narcissistic = lambda n: sum([int(d) ** len(str(n)) for d in list(str(n))]) == n
