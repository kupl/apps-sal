def interpreter(tape, code):
    tape, code = [int(t) for t in tape], [int(a) for a in code]
    ptr, out = 0, ""
    while ptr < len(code):
        try:
            for t in tape:
                if t == 1:
                    code[ptr] ^= 1
                elif t == 0:
                    ptr += 1
        except:
            break
    return ''.join(map(str, code))
