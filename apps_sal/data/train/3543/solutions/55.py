import re
def increment_string(strng):
    if not strng or not strng[-1].isdigit(): return strng + '1'
    num = re.match('.*?([0-9]+)$', strng).group(1)
    return strng[:-len(str(num))] + str(int(num)+1).zfill(len(str(num)))

