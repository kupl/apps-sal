import re

def increment_string(strng):
    s = list([_f for _f in re.split(r'(\d+)', strng) if _f])
    if not s or not s[-1].isdigit():
        return strng + '1'
    else:
        return ''.join(s[:-1]) + str(int(s[-1])+1).zfill(len(strng)-len(''.join(s[:-1])))

