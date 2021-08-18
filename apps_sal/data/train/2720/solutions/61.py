def solution(digits):
    numli = []
    if len(digits) > 5:
        for ind in range(len(digits)):
            if ind <= len(digits) - 5:
                num = digits[ind:ind + 5]
                numli.append(num)
    elif len(digits) <= 5:
        numli.append[0]

    return int(max(numli))
