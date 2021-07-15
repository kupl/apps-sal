import re
from random import randint as d
def roll(desc, verbose=False):
    try:
        desc=desc.replace(' ','')
        if desc[0] =='d': desc= '1'+desc
        s=re.search('^(\d+)d(\d+)(([+-]?\d+)*)$',desc).groups()
        m = eval(s[2]) if s[2] != '' else 0 
        res = { 'dice': [d(1,int(s[1]))] * int(s[0]), 'modifier': m }
        return res if verbose else sum(res['dice'])+res['modifier']
    except:
        return False

