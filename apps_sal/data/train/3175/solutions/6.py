import re


def triple_double(*args):
    return bool(re.search('(\\d)(\\1){2}.*\\ .*(\\1){2}', '%s %s' % args))
