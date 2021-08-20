import re
HL = {'R+': 'green', 'F+': 'pink', 'L+': 'red', '\\d+': 'orange'}
PATTERN_HL = re.compile('|'.join(HL))
HL_FORMAT = '<span style="color: {}">{}</span>'


def replacment(m):
    (s, k) = (m.group(), m.group()[0] + '+')
    return HL_FORMAT.format(HL[k], s) if k in HL else HL_FORMAT.format(HL['\\d+'], s) if s.isdigit() else s


def highlight(code):
    return PATTERN_HL.sub(replacment, code)
