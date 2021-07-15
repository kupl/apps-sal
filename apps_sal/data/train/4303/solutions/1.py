def sum_arrangements(num):
    import math
    numLength = len(str(num))
    scaleFactor = int("1"*numLength) * math.factorial(numLength - 1)
    ans = 0
    for i in range(numLength):
        num, digit = divmod(num, 10)
        ans = ans + digit
    return ans * scaleFactor
