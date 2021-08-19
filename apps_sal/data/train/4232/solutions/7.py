def convert_to_mixed_numeral(parm):
    lis = list(map(int, parm.split('/')))
    whole = abs(lis[0]) // lis[1]
    mod = abs(lis[0]) % lis[1]
    if lis[0] < 0:
        if mod == 0:
            return '-{}'.format(whole)
        elif whole != 0:
            return '-{0} {1}/{2}'.format(whole, mod, lis[1])
        else:
            return '-{0}/{1}'.format(mod, lis[1])
    elif mod == 0:
        return '{0}'.format(whole)
    elif whole != 0:
        return '{0} {1}/{2}'.format(whole, mod, lis[1])
    else:
        return '{0}/{1}'.format(mod, lis[1])
