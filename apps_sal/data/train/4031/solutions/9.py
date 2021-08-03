def interpreter(code, tape):
    pos = 0
    tape = list(map(int, list(tape)))
    pos_code = 0
    while pos_code < len(code) and pos < len(tape) and pos > -1:
        instruction = code[pos_code]
        if instruction == '>':
            pos += 1
        elif instruction == '<':
            pos -= 1
        elif instruction == '*':
            if tape[pos] == 0:
                tape[pos] = 1
            else:
                tape[pos] = 0
        elif instruction == '[':
            if tape[pos] == 0:
                open = 1
                for i in range(pos_code + 1, len(code)):
                    if code[i] == '[':
                        open += 1
                    elif code[i] == ']':
                        open -= 1
                        if open == 0:
                            pos_code = i
                            break

        elif instruction == ']':
            if tape[pos] != 0:
                closed = 1
                for i in range(pos_code - 1, -1, -1):
                    if code[i] == ']':
                        closed += 1
                    elif code[i] == '[':
                        closed -= 1
                        if closed == 0:
                            pos_code = i
                            break
        pos_code += 1
    return ''.join(map(str, tape))
