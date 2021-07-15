import re

def to_integer(string):
    try: return eval(''.join(e for e in re.match(r'\A([-+]?)(?:(0b[01]+)|(0o[0-7]+)|(0x[0-9a-fA-F]+)|0*(\d+))\Z',string).groups() if e))
    except: return None
