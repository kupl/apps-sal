from string import ascii_lowercase as l, ascii_uppercase as u
a, r = f"{l}{u}", lambda s, m: f"{s[m:]}{s[:m]}"


def encryptor(k, m):
    return m.translate(str.maketrans(a, "".join(r(s, k % 26) for s in (l, u))))
