import re


def original_number(s):
    return ''.join((n * str(i) for (i, n) in enumerate(eval(re.sub('([A-Z])', 's.count("\\1")', '[Z,O-W-U-Z,W,H-G,U,F-U,X,S-X,G,I-G-F+U-X]')))))
