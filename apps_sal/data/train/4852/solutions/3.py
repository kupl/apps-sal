def interpreter(tape):
    out = []
    stack = [0]
    ip = 0
    while ip < len(tape):
        cmd = tape[ip]
        if cmd == '^': stack.pop()
        elif cmd == '!': stack.append(0)
        elif cmd == '+': stack[-1] = (stack[-1] + 1)  % 256
        elif cmd == '-': stack[-1] = (stack[-1] - 1)  % 256
        elif cmd == '*': out.append(chr(stack[-1]))
        elif cmd == '[':
            if stack[-1] == 0:
                while tape[ip] != ']': ip += 1
        elif cmd == ']':
            if stack[-1] != 0:
                while tape[ip] != '[': ip -= 1
        ip += 1
    return ''.join(out)

