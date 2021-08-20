def primeFactors(n):
    list = []
    for i in range(2, round(n ** 0.5)):
        while (n / i).is_integer():
            n /= i
            list.append(i)
    if len(list) < 2:
        list.append(int(n))
    list_seen = []
    str1 = ''
    for x in list:
        if x in list_seen:
            pass
        else:
            list_seen.append(x)
            if list.count(x) > 1:
                str1 += f'({str(x)}**{str(list.count(x))})'
            else:
                str1 += '(' + str(x) + ')'
    return str1
