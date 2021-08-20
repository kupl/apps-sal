import re


def domain_name(url):
    pat = '(http[s]?://)*(www\\.)*(\\w+[-_]*\\w+)\\b(\\..*)'
    res = re.match(pat, url)
    return str(res.group(3))
