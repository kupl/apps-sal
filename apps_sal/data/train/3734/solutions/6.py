import re #who needs random!
def roll(desc, v=False):
    try:
        q,d,m = re.search('^(\d*)d(\d+)(.*)$',desc.replace(' ','')).groups()
        r = [int(d)]*int(q or 1)
        m = eval(re.search('^(([+-]\d+)+)$',m).groups()[0]) if m else 0
        return { 'dice': r, 'modifier': m } if v else sum(r)+m
    except:
        return False
