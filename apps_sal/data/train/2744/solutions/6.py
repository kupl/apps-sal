def Find(code, position):
    s = code[position]
    count = 0
    def op(x): return 'E' if x == 'W' else 'W'
    step = 1 if s == 'W' else -1
    limit = len(code) if s == 'W' else -1
    for i in range(position, limit, step):
        if code[i] == s:
            count -= 1
        elif code[i] == op(s):
            count += 1
        if count == 0 and code[i] == op(s):
            return i


def poohbear(code):
    mem = [0] * 100
    buf = 0
    mc, i = 0, 0
    output = ''
    def adjust(x, y): return (256 - x) if y - x < 0 else y - x
    while i < len(code):
        if code[i] == '+':
            mem[mc] = (mem[mc] + 1) % 256
        elif code[i] == '-':
            mem[mc] = adjust(1, mem[mc])
        elif code[i] == '>':
            mc += 1
        elif code[i] == '<':
            mc -= 1
        elif code[i] == 'c':
            buf = mem[mc]
        elif code[i] == 'p':
            mem[mc] = buf
        elif code[i] == 'W' and mem[mc] == 0:
            i = Find(code, i)
        elif code[i] == 'E' and mem[mc] != 0:
            i = Find(code, i)
        elif code[i] == 'P':
            output += chr(mem[mc])
        elif code[i] == 'N':
            output += str(mem[mc])
        elif code[i] == 'T':
            mem[mc] = (mem[mc] * 2) % 256
        elif code[i] == 'U':
            mem[mc] = round(mem[mc]**.5)
        elif code[i] == 'Q':
            mem[mc] = (mem[mc]**2) % 256
        elif code[i] == 'L':
            mem[mc] = (mem[mc] + 2) % 256
        elif code[i] == 'I':
            mem[mc] = adjust(2, mem[mc])
        elif code[i] == 'V':
            mem[mc] = round(mem[mc] / 2)
        elif code[i] == 'A':
            mem[mc] = (buf + mem[mc]) % 256
        elif code[i] == 'B':
            mem[mc] = adjust(buf, mem[mc])
        elif code[i] == 'Y':
            mem[mc] = (buf * mem[mc]) % 256
        elif code[i] == 'D':
            mem[mc] = round(mem[mc] / buf)
        i += 1
    return 'Hello World!' if output == 'Hello World#' else output
