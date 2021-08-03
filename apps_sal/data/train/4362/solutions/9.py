import re


def frogify(s):
    t = re.split(r'(\W+)', s)[:-1]
    if len(t) == 0:
        return ''
    t = [re.sub(r'[ ]*[,;:()-]', '', s) for s in t]
    t = [(s, ' ')[s == ''] for s in t]
    while t[0] == ' ':
        t.pop(0)
    matches = [j for j, x in enumerate(t) if x[0] in '.?!']
    oldi = 0
    for i in matches:
        t[oldi:i] = t[oldi:i][::-1]
        oldi = i + 1
    return ''.join(t)
