from collections import Counter

def primeFactors(number):
    ret, i = [], 2
    while i <= number:
        if number % i == 0:
            ret.append(i)
            number = number // i
            continue
        if i is not 2:
            i += 2
        else:
            i += 1
    count = Counter(ret)
    ret_string = []
    for key in sorted(count):
        ret_string.append('({})'.format(key)) if count[key] == 1 else ret_string.append('({}**{})'.format(key, count[key]))

    return ''.join(ret_string)
