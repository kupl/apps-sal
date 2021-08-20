import re


def pete_talk(*args):
    speech = args[0].lower()
    permitted = args[1] if len(args) == 2 else []
    speech = re.sub('([!\\?\\.] )(\\w+)', upper, speech)
    speech = re.sub('^(\\w)', upper, speech)
    speech = re.sub('(\\w{3,})', lambda match: bleep(match, permitted), speech)
    return speech


def bleep(match, perm):
    st = match.group(1)
    bleeped = st[0] + '*' * (len(st) - 2) + st[-1]
    return bleeped if st.lower() not in [x.lower() for x in perm] else st


def upper(match):
    groups = list(match.groups())
    groups[-1] = groups[-1].capitalize()
    return ''.join(groups)
