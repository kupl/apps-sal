def char_check(txt, mx, spc):
    if not spc:
        txt = txt.replace(' ', '')
    return [len(txt) <= mx, txt[:mx]]


charCheck = char_check
