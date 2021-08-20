def primeFactors(n):
    i = 2
    li = []
    s = ''
    while n != 1:
        count = 0
        while n % i == 0:
            n = n / i
            count = count + 1
        if count != 0:
            re = (i, count)
            li.append(re)
        i = i + 1
    for i in li:
        if i[1] != 1:
            s = s + '(' + str(i[0]) + '**' + str(i[1]) + ')'
        else:
            s = s + '(' + str(i[0]) + ')'
    return s
