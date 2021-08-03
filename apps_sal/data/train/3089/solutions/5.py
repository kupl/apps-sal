import re


def dashatize(num):
    lst = re.findall(r'[13579]|[02468]+', str(num))
    return '-'.join(lst) if lst else 'None'
