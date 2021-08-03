import scipy as sc
import scipy.optimize as so


def original_number(s):
    return ''.join([str(k) * int(round(n)) for k, n in enumerate(
        so.nnls(sc.transpose([sc.histogram([ord(c) - 65 for c in d], list(range(27)))[0] for d in
                              ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
                              ]), sc.histogram([ord(c) - 65 for c in s], list(range(27)))[0])[0])])
