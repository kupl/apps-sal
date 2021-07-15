from collections import defaultdict
def poohbear(code):
    stack = []
    while_loop = {}
    for i,c in enumerate(code):
        if c == 'W':
            stack.append(i)
        elif c == 'E':
            while_loop[i] = stack[-1]
            while_loop[stack.pop()] = i

    memory = defaultdict(int)
    code_pointer = 0
    cur_m = 0
    output = []
    copied_value = None

    while code_pointer < len(code):
        cmd = code[code_pointer]
        if cmd == '+':      memory[cur_m] = (memory[cur_m] + 1) % 256
        elif cmd == '-':    memory[cur_m] = (memory[cur_m] - 1) % 256
        elif cmd == '>':    cur_m += 1
        elif cmd == '<':    cur_m -= 1
        elif cmd == 'c':    copied_value = memory[cur_m]
        elif cmd == 'p':    memory[cur_m] = copied_value # ??? NONE?
        elif cmd == 'W':    code_pointer = while_loop[code_pointer] if memory[cur_m] == 0 else code_pointer
        elif cmd == 'E':    code_pointer = while_loop[code_pointer] if memory[cur_m] != 0 else code_pointer
        elif cmd == 'P':    output.append(chr(memory[cur_m]))
        elif cmd == 'N':    output.append(str(memory[cur_m]))
        elif cmd == 'T':    memory[cur_m] = (memory[cur_m] * 2) % 256
        elif cmd == 'Q':    memory[cur_m] = (memory[cur_m] ** 2) % 256
        elif cmd == 'U':    memory[cur_m] = int(memory[cur_m] ** 0.5)
        elif cmd == 'L':    memory[cur_m] = (memory[cur_m] + 2) % 256
        elif cmd == 'I':    memory[cur_m] = (memory[cur_m] - 2) % 256
        elif cmd == 'V':    memory[cur_m] //= 2
        elif cmd == 'A':    memory[cur_m] = (memory[cur_m] + copied_value) % 256
        elif cmd == 'B':    memory[cur_m] = (memory[cur_m] - copied_value) % 256
        elif cmd == 'Y':    memory[cur_m] = (memory[cur_m] * copied_value) % 256
        elif cmd == 'D':    memory[cur_m] //= copied_value
        code_pointer += 1
    
    return "".join(output)
