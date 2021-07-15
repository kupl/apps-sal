import re

def increment_string(strng):
    array = re.findall(r'[0-9]+', strng)
    if array:
        size=len(array[-1])
        num=str(int(array[-1])+1)
        base=strng[0:-size]
        while len(num)<size:
            num='0'+num
        return base+num
    else:
        return strng+'1'
    return strng
