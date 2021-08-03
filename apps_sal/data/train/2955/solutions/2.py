def oddest(A): return max(A, key=lambda x: bin(256 + x)[::-1])
