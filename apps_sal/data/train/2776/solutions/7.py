def commas(num):
    return str('{:,.3f}'.format(num)).rstrip('0').rstrip('.')
