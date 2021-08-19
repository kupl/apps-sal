def interpreter(code, t):
    print((code, t))
    tape = list(t)
    f = [n for (n, x) in enumerate(list(code)) if x == '[']
    l = [n for (n, x) in enumerate(list(code)) if x == ']']
    l.reverse()
    print((f, l))
    (i, x, curr) = (0, 0, 0)
    while i != len(code) and x > -1 and (x < len(tape)):
        if x > -1 and x < len(tape):
            curr = int(tape[x])
        if code[i] == '>':
            x += 1
        if code[i] == '<':
            x -= 1
        if code[i] == '*' and x > -1 and (x < len(tape)):
            if tape[x] == '1':
                tape[x] = '0'
            else:
                tape[x] = '1'
        if code[i] == '[' and curr == 0:
            if f != None:
                i = l[f.index(i)]
            else:
                break
        elif code[i] == ']' and curr == 1:
            if l != None:
                i = f[l.index(i)]
            else:
                break
        i += 1
    return ''.join(tape)
