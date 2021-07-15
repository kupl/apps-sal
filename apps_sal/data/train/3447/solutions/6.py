def next_perfect_square(n, i=0):
    while True:
        if i*i > n: return i*i
        i += 1
