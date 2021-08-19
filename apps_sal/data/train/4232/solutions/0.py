def convert_to_mixed_numeral(parm):
    (a, b) = list(map(int, parm.split('/')))
    (d, r) = divmod(abs(a), b)
    s = (0 < a) - (a < 0)
    return parm if d == 0 else ('{}' + ' {}/{}' * (r != 0)).format(d * s, r, b)
