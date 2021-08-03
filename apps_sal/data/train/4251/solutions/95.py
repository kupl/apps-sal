def difference_of_squares(n):

    return (sum(x for x in range(n + 1)) * sum(x for x in range(n + 1))) - sum(x * x for x in range(n + 1))
