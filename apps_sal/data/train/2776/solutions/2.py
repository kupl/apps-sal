import re

def commas(num):
    if isinstance(num, int):
        return format(num, ',')
    else:
        return re.sub('\.?0+$', '', format(round(num, 3), ',.3f'))

