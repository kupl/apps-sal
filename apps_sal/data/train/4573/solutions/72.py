def over_the_road(address, n):
    #     the sum of the right side of the node is[1,3,5,.....,2n-1]
    #     the sum of the left side of the node is [2n,2n-2,...,2]
    return (2 * n + 1 - address)
    pass
