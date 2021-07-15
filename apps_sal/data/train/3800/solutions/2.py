import re
from string import ascii_uppercase as ALPHA

def num2alpha(num, b=len(ALPHA), numerals=ALPHA):
    return '' if not num else (num2alpha((num-1) // b, b, numerals) + numerals[(num-1) % b])
def alpha2num(string, b=len(ALPHA), numerals=ALPHA):
    return sum((numerals.index(v)+1)*b**i for i,v in enumerate(reversed(string)))
    
rcregex = re.compile('R(\d+)C(\d+)')
spregex = re.compile('([A-Z]+)(\d+)')
def spreadsheet(s):
    m = rcregex.match(s)
    if m: return num2alpha(int(m.group(2)))+m.group(1)
    m = spregex.match(s)
    if m: return 'R{}C{}'.format(m.group(2),alpha2num(m.group(1)))
    return ''

