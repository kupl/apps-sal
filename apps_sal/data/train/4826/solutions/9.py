import re
def count_robots(li):
    legs, body, find = '[a-zA-Z]','[|};&#[\]/><\(\)*]', []
    a = m = 0
    for i in li:
        r = re.search(r'automatik|mechanik', i, re.I)
        if r:
            l = re.findall(r'{0}{1}{1}0{1}{1}0{1}{1}{0}'.format(legs, body), i)
            if re.search('mechanik',r.group(),re.I): m+=len(l)
            else:a+=len(l)
    return [f'{a} robots functioning automatik', f'{m} robots dancing mechanik']
