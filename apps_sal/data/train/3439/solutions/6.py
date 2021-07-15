solve = lambda n: sum(map(int, str(n - int('0' + '9' * (len(str(n))-1))))) + 9 * (len(str(n)) - 1)
