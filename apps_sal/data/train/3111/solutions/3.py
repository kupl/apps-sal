def number_format(n):
    return str('{:,.3f}'.format(n)).rstrip('0').rstrip('.')
