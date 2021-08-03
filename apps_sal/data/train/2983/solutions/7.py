from scipy.special import comb


def bouncy_count(n):
    if n < 3:
        return 0
    b = 10  # Change for different bases
    incline_sum = 0
    decline_sum = 0
    for i in range(3, n + 1):
        incline_sum += comb(b + i - 1, i, exact=True) - 10
        decline_sum += comb(b + i - 2, i, exact=True)

    return b**n - b**2 - incline_sum - decline_sum
