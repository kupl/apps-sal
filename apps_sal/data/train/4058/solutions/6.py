def pattern(n):
    if n < 1: return ""
    wing = "\n".join((str(i%10) + " "*(2*(n-i) - 1) + str(i%10)).center(2*n - 1) for i in range(1, n))
    return "\n".join([wing, str(n%10).center(2*n-1), wing[::-1]])
