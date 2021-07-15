import re
def alphabet_war(fight):
    d = {a : c for c, a in enumerate('wpbs zdqm', -4) if c}
    s = sum(d.get(a, 0) for a in re.sub(r'.?\*+.?', '', fight))
    return ['Left side wins!', "Let's fight again!", 'Right side wins!'][1 + min(max(s, -1), 1)]
