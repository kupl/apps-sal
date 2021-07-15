import re

POWERS  = {c:i for i,c in enumerate('wpbs zdqm',-4)}
PATTERN = re.compile(r'(?<!\*)([{}])(?!\*)'.format(''.join(POWERS.keys()-{' '})))

def alphabet_war(fight):
    s = sum(POWERS[c] for c in PATTERN.findall(fight))
    return ["Let's fight again!", 'Left side wins!', 'Right side wins!'][ (s<0) - (s>0) ]
