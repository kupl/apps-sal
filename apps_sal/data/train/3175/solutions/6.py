import re


def triple_double(*args):
    return bool(re.search(r'(\d)(\1){2}.*\ .*(\1){2}', '%s %s' % args))
