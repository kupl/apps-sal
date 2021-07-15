import re
from operator import itruediv,imul,isub,iadd
def calculate_string(st):
    op=itruediv if '/' in st else iadd if '+' in st else isub if '-' in st else imul
    l=[eval(''.join(re.findall('[\d.]',s))) for s in re.split('[-+*/]',st)]
    return str(round(op(l[0],l[1])))
