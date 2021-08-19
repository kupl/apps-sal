def sum_of_integers_in_string(s):
    che = '0123456789'
    tmp = ''
    res = []
    for i in range(len(s)):
        if s[i] in che:
            tmp += s[i]
            if i == len(s) - 1:
                res.append(int(tmp))
        elif tmp != '':
            res.append(int(tmp))
            tmp = ''
    return sum(res)
