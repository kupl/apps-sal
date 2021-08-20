def convert_to_mixed_numeral(parm):
    (sign, parm) = (parm[:'-' in parm], parm['-' in parm:])
    (numerator, denominator) = parm.split('/')
    (integer, numerator) = divmod(int(numerator), int(denominator))
    (integer, fraction) = (f"{integer or ''}", f'{numerator}/{denominator}' if numerator else '')
    return f"{sign}{integer}{(integer and fraction) and ' '}{fraction}"
