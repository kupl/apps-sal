import re

pattern = re.compile(r"[@\.]")
obfusc = {'@': " [at] ", '.': " [dot] "}.get


def obfuscate(email):
    return pattern.sub(lambda x: obfusc(x.group()), email)
