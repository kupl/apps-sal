import re

def reverse(strng): return re.sub(r'(\w)\1+', lambda m: m.group().swapcase(), strng)
