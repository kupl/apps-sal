def unlucky_number(n): return sum(not {'4', '7'} & set(str(x)) for x in range(0, n + 1, 13))
