def jumps(code):
    stack = []
    skip_to = dict()
    return_to = dict()
    for i, c in enumerate(code):
        if c == '[':
            stack.append(i)
        elif c == ']':
            opening, closing = stack.pop(), i
            skip_to[opening] = closing
            return_to[closing] = opening
    return (skip_to, return_to)

def run_one_instruction(code, tape, pc, pointer, skip_to, return_to):
    instruction = code[pc]
    if instruction == '>':
        pointer += 1
    elif instruction == '<':
        pointer -= 1
    elif instruction == '*':
        tape[pointer] ^= 1
    elif instruction == '[':
        if tape[pointer] == 0:
            pc = skip_to[pc]
    elif instruction == ']':
        if tape[pointer]:
            pc = return_to[pc]
    return (pc, pointer)

def should_terminate(pc, max_pc, pointer, max_pointer):
    return pc > max_pc or pointer < 0 or pointer > max_pointer

def interpreter(code, tape):
    tape = [int(c) for c in tape]
    max_pointer = len(tape) - 1
    pointer = 0
    max_pc = len(code) - 1
    pc = 0
    skip_to, return_to = jumps(code)
    while not should_terminate(pc, max_pc, pointer, max_pointer):
        pc, pointer = run_one_instruction(code, tape, pc, pointer, skip_to, return_to)
        pc += 1
    return ''.join(str(cell) for cell in tape)
