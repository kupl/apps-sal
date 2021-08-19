import re


def obfuscate(email):
    return re.sub('[@\\.]', lambda match: ' [at] ' if match.group(0) == '@' else ' [dot] ', email)
