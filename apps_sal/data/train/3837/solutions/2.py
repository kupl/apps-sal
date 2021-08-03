f = reverse = lambda A: len(A) == 1 and A or f([x - y for x, y in zip(A, A[1:])]) + [A[-1]]
