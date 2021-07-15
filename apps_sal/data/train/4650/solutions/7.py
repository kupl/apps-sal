import re

nums = '1234567890'

def validPhoneNumber(pn):
    if len(pn) != len("(123) 456-7890"):
        return False  
    elif pn[0] != '(':
        return False
    elif pn[1] not in nums or pn[2] not in nums or pn[3] not in nums:
        return False
    elif pn[4] != ')':
        return False
    elif pn[5] != ' ':
        return False
    elif pn[6] not in nums or pn[7] not in nums or pn[8] not in nums:
        return False
    elif pn[9] != '-':
        return False
    elif pn[10] not in nums or pn[11] not in nums or pn[12] not in nums or pn[13] not in nums:
        return False
    else:
        return True
