def cumulative_triangle(n):
    # find last number (x) of nth row
    x = sum(range(n + 1))
    # add all numbers from (x-n, x)
    return sum(range(x - n + 1, x + 1))
