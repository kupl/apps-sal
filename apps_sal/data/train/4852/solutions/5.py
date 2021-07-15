def interpreter(tape):
    stack, output = [0], ''
    i, n = 0, len(tape)
    while i < n:
        cmd = tape[i]
        if cmd == '^':
            stack.pop()
        elif cmd == '!':
            stack.append(0)
        elif cmd == '+':
            stack[0] = 0 if stack[0] == 255 else stack[0] + 1
        elif cmd == '-':
            stack[0] = 255 if stack[0] == 0 else stack[0] - 1
        elif cmd == '*':
            output += chr(stack.pop(0))
        elif cmd == '[' and stack[0] == 0:
            while tape[i] != ']':
                i += 1
        elif cmd == ']' and stack[0] != 0:
            while tape[i] != '[':
                i -= 1
        i += 1
    return output.replace('\n', '\x02')
