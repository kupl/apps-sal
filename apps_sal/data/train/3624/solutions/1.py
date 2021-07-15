def distribution_of_candy(candies):
    n = 0
    while any(c != candies[0] for c in candies):
        n += 1
        half = [(c+1)//2 for c in candies]
        candies = [a+b for a, b in zip(half, half[-1:] + half[:-1])]
    return [n, candies[0]]
