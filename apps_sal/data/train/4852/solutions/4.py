def interpreter(tape):
    ptr, stack, output = 0, [0], ''
    n = len(tape)

    while ptr < n:

        cmd = tape[ptr]

        if cmd == '^':
            stack.pop()
        elif cmd == '!':
            stack.append(0)
        elif cmd == '+':
            stack[-1] = (stack[-1] + 1) % 256
        elif cmd == '-':
            stack[-1] = (stack[-1] + 255) % 256
        elif cmd == '*':
            output += chr(stack[-1])
        elif cmd == '[' and stack[-1] == 0:
            while tape[ptr] != ']':
                ptr += 1
        elif cmd == ']' and stack[-1] != 0:
            while tape[ptr] != '[':
                ptr -= 1

        ptr += 1

    return output
