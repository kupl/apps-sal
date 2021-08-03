import re


def spin_solve(sentence):
    ans = sentence.split()
    for idx, val in enumerate(ans):
        t = re.sub('[^\w-]', '', val)
        if len(t) > 6 or t.lower().count('t') > 1:
            ans[idx] = t[::-1] + val[len(t):]
        elif len(t) == 2 or val.endswith(','):
            ans[idx] = val.upper()
        elif len(t) == 1:
            ans[idx] = '0'
    return ' '.join(ans)
