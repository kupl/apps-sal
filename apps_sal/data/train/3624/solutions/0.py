def distribution_of_candy(candies):
    steps = 0
    while len(set(candies)) > 1:
        candies = [(a + 1) // 2 + (b + 1) // 2 for (a, b) in zip(candies, candies[-1:] + candies)]
        steps += 1
    return [steps, candies.pop()]
