def distribution_of_candy(candies):
    r = 0
    while len(set(candies)) > 1:
        r += 1
        candies = [(c+1)//2 + (candies[i-1]+1)//2 for i,c in enumerate(candies)]

    return [r, candies[0]]
