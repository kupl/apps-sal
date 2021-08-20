def count_divisors(n):
    """Counts the integer points under the parabola xy = n.

    Because the region is symmetric about x = y, it is only necessary to sum up
    to that point (at n^{1/2}), and double it. By this method, a square region is
    counted twice, and thus subtracted off the total.
    """
    r = int(n ** (1 / 2))
    return 2 * sum((n // i for i in range(1, r + 1))) - r * r
