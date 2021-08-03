import string


def position(alphabet):
    al = list(enumerate(list(string.ascii_lowercase), 1))
    d = {}
    for e in al:
        x = {e[1]: e[0]}
        d.update(x)
    return 'Position of alphabet: ' + str(d[alphabet])
