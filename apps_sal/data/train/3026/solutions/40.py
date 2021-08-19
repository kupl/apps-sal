def min_value(digits):
    newDigits = []
    for i in digits:
        if i not in newDigits:
            newDigits.append(i)
    sortDigits = sorted(newDigits)
    strDigits = [str(i) for i in sortDigits]
    return int(''.join(strDigits))
