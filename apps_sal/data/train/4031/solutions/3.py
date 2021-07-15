def interpreter(code, tape):
    p = 0
    c = 0
    li = list(tape)
    left = {}
    right = {}
    stk = []
    for x in range(len(code)):
        if code[x] == '[':
            stk.append(x)
        elif code[x] == ']':
            sb = stk.pop()
            left[str(sb)] = x
            right[str(x)] = sb
    while c < len(code):
        if p < 0 or p >= len(tape):
            return ''.join(li)
        if code[c] == '[':
            if li[p] == '0':
                c = left[str(c)]
        elif code[c] == ']':
            if li[p] != '0':
                c = right[str(c)]
        elif code[c] == '*':
            li[p] = str(abs(int(li[p])-1))
        elif code[c] == '>':
            p += 1
        elif code[c] == '<':
            p -= 1
        c += 1
    return ''.join(li)
