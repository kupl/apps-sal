def sum_digits(num):
    return sum([int(d) for d in num])


def order_weight(string):
    if string == '':
        return string
    weights = [(sum_digits(num), num) for num in string.split()]
    weights.sort()
    answer = [weights[i][1] for (i, _) in enumerate(weights)]
    return ' '.join(answer)
