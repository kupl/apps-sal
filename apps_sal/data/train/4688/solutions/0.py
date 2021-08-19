def expanded_form(num):
    (integer_part, fractional_part) = str(num).split('.')
    result = [str(int(num) * 10 ** i) for (i, num) in enumerate(integer_part[::-1]) if num != '0'][::-1]
    result += [str(num) + '/' + str(10 ** (i + 1)) for (i, num) in enumerate(fractional_part) if num != '0']
    return ' + '.join(result)
