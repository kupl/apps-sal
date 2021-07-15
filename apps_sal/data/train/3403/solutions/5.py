reorder = lambda a, b: [x[-b%len(x):] + x[:-b%len(x)] for x in map(list, (range(a//2), range(a//2, a)))]
