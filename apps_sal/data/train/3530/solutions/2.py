import re
def asterisc_it(n): 
    s = ''.join(map(str, n)) if isinstance(n, list) else str(n)
    return re.sub('([02468])(?=[02468])', r'\1*', s)
