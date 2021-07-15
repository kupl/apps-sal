import re
def parse_mana_cost(mana):
        retval = {}
        mana = mana.lower()
        m = re.match(r'\A(\d*)([wubrg]*)\Z', mana)
        if m:
                if m.group(1) and int(m.group(1)) > 0:
                                retval['*'] = int(m.group(1))
                if m.group(2):
                        l = list(m.group(2))
                        print(l)
                        if l.count('w') > 0:
                                retval['w'] = l.count('w')
                        if l.count('u') > 0:
                                retval['u'] = l.count('u')
                        if l.count('b') > 0:
                                retval['b'] = l.count('b')
                        if l.count('r') > 0:
                                retval['r'] = l.count('r')
                        if l.count('g') > 0:
                                retval['g'] = l.count('g')
                return retval

