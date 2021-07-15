from scipy.special import comb

def bouncy_count(n):
    return 10 ** n - comb(n + 9, n, exact=True) - comb(n + 10, n, exact=True) + 1 + n * 9 + n
