D_S = '0123456789abcdef'
S_D = {d: n for n, d in enumerate(D_S)}


def convert(s, bIn, bOut):
    n = sum(S_D[d] * bIn**p for p, d in enumerate(reversed(s.lower())))
    out = []
    while n:
        n, r = divmod(n, bOut)
        out.append(D_S[r])
    return ''.join(reversed(out)) or '0'


def bin_to_hex(s): return convert(s, 2, 16)
def hex_to_bin(s): return convert(s, 16, 2)
