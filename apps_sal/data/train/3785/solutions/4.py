# C(n, k) == n!/(k!(n-k)!) simplifies to  a/b
# where    a ==  n*(n-1)*(n-2)*...*(n-(k-2))*(n-(k-1))
#          b ==  (k-1)!
def efficientCombination(n, k):
    from math import gcd

    # a and b are defined in above comment
    a, b = 1, 1

    if k == 0:
        return 1

    # Since C(n,k) == C(n,n-k), so take n-k when it's smaller than k
    if n - k < k:
        k = n - k

    while k:
        a *= n
        b *= k

        m = gcd(a, b)
        a //= m
        b //= m

        n -= 1
        k -= 1
    # ---end while

    return a

# -----end function


# d is the deisred diagonal from right to left (starting count at 0), and amt is
# the number of elements desired from that diagonal
def generate_diagonal(d, amt):
    diagElements = []

    for n in range(d, amt + d, 1):
        valOnDiag = efficientCombination(n, d)
        diagElements.append(valOnDiag)

    return diagElements

# ---end function
