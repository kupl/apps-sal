def interpreter(tape):
    (data, pos, res) = ([0 for i in range(tape.count('*'))], 0, '')
    while 1:
        try:
            for i in iter([i for i in tape]):
                if i == '+':
                    data[pos] = (data[pos] + 1) % 256
                elif i == '-':
                    data[pos] = (data[pos] - 1) % 256
                elif i == '>':
                    pos += 1
                elif i == '<':
                    pos -= 1
                elif i == '*':
                    res += chr(data[pos])
                elif i == '/' and data[pos] == 0:
                    next(tape)
                elif i == '\\' and data[pos] != 0:
                    next(tape)
                elif i == '&':
                    return res
        except:
            pass
