from scipy.special import comb


def bouncy_count(number):
    return 10**number + 10 * number + 1 - comb(10 + number, 10, True) - comb(9 + number, 9, True)
