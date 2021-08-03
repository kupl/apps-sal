def balanced_num(number):
    s = list(map(int, str(number)))
    return ['Not Balanced', 'Balanced'][sum(s[:(len(s) - 1) // 2]) == sum(s[((len(s) - 1) // 2) + 1 + (len(s) % 2 == 0):])]
