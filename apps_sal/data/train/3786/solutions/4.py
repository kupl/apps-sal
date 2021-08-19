RULES = [['ci si', 'ce se', 'c(?!h) k'], ['ph f'], ['(?<=\\w{3})e+\\b ', '([a-z])\\1 \\1'], ['th z', 'wr r', 'wh v', 'w v'], ['ou u', 'an un', 'ing\\b ink', '\\bsm schm']]


def siegfried(week, txt):
    import re

    def keep_case(repl):

        def wrapper(m):
            ref = re.match('\\\\(\\d)', repl)
            strng = m.group(int(ref.group(1))) if ref else repl
            g = m.group(0)
            if g.islower():
                return strng.lower()
            if g.isupper():
                return strng.upper()
            if g.istitle():
                return strng.title()
            return strng
        return wrapper
    for rules in RULES[:week]:
        for rule in rules:
            (src, repl) = rule.split(' ')
            txt = re.sub(src, keep_case(repl), txt, flags=re.I)
    return txt
