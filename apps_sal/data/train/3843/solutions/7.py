from string import ascii_lowercase as l, ascii_uppercase as u, digits as di
def encrypt(s): return doall(s)


def decrypt(s): return doall(s, True)


def doall(s, d=False):
    if not s:
        return s
    all_char = list(u + l + di + ".,:;-?! '()$%&" + '"')
    s = "".join([j.swapcase() if i & 1 else j for i, j in enumerate(s)]) if not d else s
    new, well = [], [all_char[-1 - all_char.index(s[0])]]
    for i in range(len(s) - 1):
        c_ = well[-1] if d else s[i]
        t_ = s[i + 1]
        diff = all_char.index(c_) - all_char.index(t_)
        well.append(all_char[diff])
        new.append(all_char[diff])
    encode = all_char[-1 - all_char.index(s[0])] + "".join(new)
    decode = "".join([j.swapcase()if i & 1 else j for i, j in enumerate("".join(well))])
    return [encode, decode][d]
