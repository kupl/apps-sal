def min_value(digits):
    num1 = ''
    digits = sorted(digits)
    stringints = [str(int) for int in digits]
    for i in stringints:
        if i not in num1:
            num1 += i
    return int(num1)
