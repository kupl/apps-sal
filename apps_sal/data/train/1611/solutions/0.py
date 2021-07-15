from collections import defaultdict
from itertools import chain
import re

PARSE = re.compile(r'[pP]\d+|q')

def magic_call_depth_number(prog):
    
    def parse(it, p=''):
        for m in it:
            if m[0].startswith('p'): parse(it, m[0])
            elif m[0]=='q':          return
            else:                    pCmds[p].append(m[0].lower())
    
    def travel(p, seen, d=1):
        if not pCmds[p]:
            yield 0
        else:
            for n in pCmds[p]:
                if n in seen: yield d
                else:         yield from travel(n, seen|{n}, d+1)
    
    pCmds = defaultdict(list)
    parse(PARSE.finditer(prog))
    inf = list(chain.from_iterable(travel(p, {p}) for p in pCmds['']))
    
    return [min(inf, default=0), max(inf, default=0)]

