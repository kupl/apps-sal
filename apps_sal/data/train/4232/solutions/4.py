def convert_to_mixed_numeral(frac):
    (numerator, denominator) = (int(a) for a in frac.split('/'))
    (quo, rem) = divmod(abs(numerator), denominator)
    signed_quo = -quo if numerator < 0 else quo
    if quo == 0:
        return frac
    elif rem == 0:
        return '{}'.format(signed_quo)
    return '{}{}/{}'.format('{} '.format(signed_quo) if quo > 0 else '', rem, denominator)
