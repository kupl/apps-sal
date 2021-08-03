def oddest(A): return max(A, key=lambda x: f'{x+256:b}'[::-1])
