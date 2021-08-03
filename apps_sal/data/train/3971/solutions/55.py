def tidyNumber(n):
    digits = [int(i) for i in str(n)]
    return all([digits[i] <= digits[i + 1] for i in range(len(digits) - 1)])
