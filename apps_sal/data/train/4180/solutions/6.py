def lottery(s):
    re = ''.join(c for c in dict.fromkeys(s) if c in '0123456789')
    return 'One more run!' if re=='' else re
