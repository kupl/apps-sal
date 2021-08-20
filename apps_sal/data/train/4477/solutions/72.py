def reverse_number(n):
    digits = 0
    num = 0
    if n >= 0:
        num = n
        sign_n = 1
    else:
        num = -n
        sign_n = -1
    while num >= 1:
        num /= 10
        digits += 1
    n = n * sign_n
    l_direct = list()
    for i in range(0, digits):
        l_direct.append(str(n % 10))
        n = int(n / 10)
        i += 1
    s = ''
    for j in range(0, digits):
        s = s + l_direct[j]
    if s == '':
        result = 0
    else:
        result = int(s) * sign_n
    return result
