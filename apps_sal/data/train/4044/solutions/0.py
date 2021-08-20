from os.path import commonprefix


def string_suffix(s):
    return sum((len(commonprefix([s, s[i:]])) for i in range(len(s))))
