import re

VOWELS = re.compile(r'[aeiuo]')

def solve(s):
    vows, cons  = sorted(VOWELS.findall(s)), sorted(VOWELS.sub('',s))
    long, short = sorted((vows, cons), key=len, reverse = True)                                                 # preserve vowels first if length are the same
    return 'failed' if len(long)-len(short) not in [0,1] else ''.join(a+b for a,b in zip(long, short+['']))
