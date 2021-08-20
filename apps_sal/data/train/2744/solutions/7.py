def poohbear(s):
    mem = [0]
    clipboard = 0
    code_pos = mem_pos = 0
    output = ''
    while code_pos != len(s):
        instr = s[code_pos]
        current = mem[mem_pos]
        result = None
        if instr == '+':
            result = current + 1
        if instr == '-':
            result = current - 1
        if instr == '>':
            mem_pos += 1
            if mem_pos == len(mem):
                mem = mem + [0]
        if instr == '<':
            mem_pos -= 1
            if mem_pos == -1:
                mem = [0] + mem
                mem_pos = 0
        if instr == 'c':
            clipboard = current
        if instr == 'p':
            result = clipboard
        if instr == 'W' and current == 0:
            depth = 1
            while depth:
                code_pos += 1
                if s[code_pos] == 'W':
                    depth += 1
                if s[code_pos] == 'E':
                    depth -= 1
        if instr == 'E' and current != 0:
            depth = 1
            while depth:
                code_pos -= 1
                if s[code_pos] == 'E':
                    depth += 1
                if s[code_pos] == 'W':
                    depth -= 1
        if instr == 'P':
            output += chr(current)
        if instr == 'N':
            output += str(current)
        if instr == 'T':
            result = 2 * current
        if instr == 'Q':
            result = current ** 2
        if instr == 'U':
            result = int(current ** 0.5)
        if instr == 'L':
            result = current + 2
        if instr == 'I':
            result = current - 2
        if instr == 'V':
            result = current // 2
        if instr == 'A':
            result = current + clipboard
        if instr == 'B':
            result = current - clipboard
        if instr == 'Y':
            result = current * clipboard
        if instr == 'D':
            result = current // clipboard
        if result is not None:
            mem[mem_pos] = result % 256
        code_pos += 1
    return output
