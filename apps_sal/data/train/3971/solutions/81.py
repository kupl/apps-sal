def tidyNumber(n):
    digits = [int(s) for s in str(n)]
    return sorted(digits) == digits
