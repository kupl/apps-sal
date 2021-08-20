import re


def siegfried(week, txt):
    if week == 1:
        txt = re.sub('ci', matchcase('si'), txt, flags=re.I)
        txt = re.sub('ce', matchcase('se'), txt, flags=re.I)
        txt = re.sub('(?!ch)[c]', matchcase('k'), txt, flags=re.I)
    elif week == 2:
        txt = siegfried(1, txt)
        txt = re.sub('ph', matchcase('f'), txt, flags=re.I)
    elif week == 3:
        txt = siegfried(2, txt)
        txt = re.sub('(?<=\\w{3})e\\b', '', txt)
        txt = re.sub('([a-z])\\1', '\\1', txt, flags=re.I)
    elif week == 4:
        txt = siegfried(3, txt)
        txt = re.sub('th', matchcase('z'), txt, flags=re.I)
        txt = re.sub('wr', matchcase('r'), txt, flags=re.I)
        txt = re.sub('wh|w', matchcase('v'), txt, flags=re.I)
    elif week == 5:
        txt = siegfried(4, txt)
        txt = re.sub('ou', 'u', txt)
        txt = re.sub('an', matchcase('un'), txt, flags=re.I)
        txt = re.sub('ing\\b', matchcase('ink'), txt, flags=re.I)
        txt = re.sub('\\bsm', matchcase('schm'), txt, flags=re.I)
    return txt


def matchcase(word):

    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace
