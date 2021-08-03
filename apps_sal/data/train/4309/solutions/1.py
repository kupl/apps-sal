import re


def replace(s):
    dic = {'!': '?', '?': '!'}
    r = re.findall(r'[!]+|[/?]+', s)
    for i in r[:]:
        ii = dic[i[0]] * len(i)
        if ii in r:
            r[r.index(ii)] = ' ' * len(i)
    return ''.join(r)
