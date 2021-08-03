def interpreter(tape):
    a, stack, out = 0, [0], []
    while a < len(tape):
        command = tape[a]
        if command == '^':
            stack.pop()
        elif command == '!':
            stack.append(0)
        elif command == '+':
            stack[-1] = (stack[-1] + 1) % 256
        elif command == '-':
            stack[-1] = (stack[-1] - 1) % 256
        elif command == '*':
            out.append(chr(stack[-1]))
        elif command == '[' and stack[-1] == 0:
            a = tape.find(']', a)
        elif command == ']' and stack[-1] != 0:
            a = tape.rfind('[', a)
        a += 1
    return ''.join(out)
