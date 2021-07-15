import re

def range_parser(s):
    return [x for r in re.split(r', *', s)
              for start,end,step in re.findall(r'(\d+)-?(\d*):?(\d*)',r) 
              for x in range(int(start), int(end or start)+1, int(step or '1'))]
