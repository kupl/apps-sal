f = reverse = lambda a: a and f([x - y for x, y in zip(a, a[1:])]) + [a[-1]]
