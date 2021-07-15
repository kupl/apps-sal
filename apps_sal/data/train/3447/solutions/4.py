from bisect import bisect
squares = [i*i for i in range(32000)]

def next_perfect_square(n):
    return bisect(squares, n)**2
