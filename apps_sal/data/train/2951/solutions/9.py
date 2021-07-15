def how_many_measurements(n, c=0): return how_many_measurements(n-2*n//3, c+1) if n > 1 else c
