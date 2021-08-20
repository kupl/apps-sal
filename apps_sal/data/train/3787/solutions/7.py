import re


def obfuscate(email):

    def substitute(m):
        if m.group(0) == '@':
            return ' [at] '
        if m.group(0) == '.':
            return ' [dot] '
    rgx = re.compile('(@|\\.)')
    return re.sub(rgx, substitute, email)
