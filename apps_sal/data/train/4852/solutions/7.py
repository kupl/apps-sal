def interpreter(tape):
    stack = [0]
    ip = 0
    output = ''
    while ip < len(tape):
        op = tape[ip]
        if op == '^':
            stack.pop()
        elif op == '!':
            stack.append(0)
        elif op == '+':
            stack[-1] = (stack[-1] + 1) % 256
        elif op == '-':
            stack[-1] = (stack[-1] + 255) % 256
        elif op == '*':
            output += chr(stack[-1])
        elif op == '[' and stack[-1] == 0:
            ip = tape.find(']', ip + 1)
        elif op == ']' and stack[-1] != 0:
            ip = tape.rfind('[', 0, ip)
        ip += 1
    return output
