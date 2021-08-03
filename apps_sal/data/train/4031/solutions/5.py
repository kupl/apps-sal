def interpreter(code, tape):
    pointer = 0
    pointer_stack = []
    code_pointer = 0
    tape_length = len(tape)
    code_length = len(code)
    tape = [c for c in tape]

    while True:
        if code_pointer >= code_length:
            break
        command = code[code_pointer]

        if command == '>':
            pointer += 1
            if pointer >= tape_length:
                break
        elif command == '<':
            pointer -= 1
            if pointer < 0:
                break
        elif command == '*':
            tape[pointer] = '0' if tape[pointer] == '1' else '1'
        elif command == '[':
            if tape[pointer] == '0':
                counter = 1
                while counter != 0:
                    code_pointer += 1
                    if code[code_pointer] == '[':
                        counter += 1
                    elif code[code_pointer] == ']':
                        counter -= 1
            else:
                pointer_stack.append(code_pointer)
        elif command == ']':
            if tape[pointer] == '1':
                code_pointer = pointer_stack[-1]
            else:
                pointer_stack.pop()
        code_pointer += 1

    return ''.join(tape)
