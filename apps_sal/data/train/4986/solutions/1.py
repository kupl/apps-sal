def f(n, m):
    # Function to return the sum of the remnainders when n is divided by m for all n from 1 to n
    # The remainders cycle from 0, 1, 2, 3,... m-1.  This happens n // m times, with a final sequnce
    # up to n % m.  The sum of 0, ... m-1 is m * (m - 1) / 2.  The sum of 0, 1, 2, 3, n % m is similar.
    #
    return (n // m) * (m - 1) * m / 2 + (n % m) * (n % m + 1) / 2
