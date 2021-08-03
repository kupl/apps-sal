def tidyNumber(n):
    digits = [x for x in str(n)]
    return True if digits == sorted(digits) else False
