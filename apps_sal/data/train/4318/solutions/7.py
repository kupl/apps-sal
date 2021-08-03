def hot_singles(A, B): return sorted(set(A) ^ set(B), key=(A + B).index)
