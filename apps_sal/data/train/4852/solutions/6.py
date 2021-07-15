def cleanTape(tape):
    a = [x for x in tape if x in '^!+-*[]']
    return ''.join(a)

def interpreter(tape):
    tape = cleanTape(tape)
    stack = [0]
    index = 0
    output = ''
    while index < len(tape):
        if tape[index] == '^':
            stack.pop()
        if tape[index] == '!':
            stack.append(0)
        if tape[index] == '+':
            stack[-1] += 1
        if tape[index] == '-':
            stack[-1] -= 1
    
        stack[-1] %= 256
    
        if tape[index] == '*':
            output += chr(stack[-1])
        
        if tape[index] == '[':
            if stack[-1] == 0:
                i = index + 1
                while True:
                    if tape[i] == ']':
                        index = i + 1
                        break
                    i += 1
                continue
        if tape[index] == ']':
            if stack[-1] != 0:
                i = index - 1
                while True:
                    if tape[i] == '[':
                        index = i - 1
                        break
                    i -= 1
                continue
        
        index += 1
        
    return output
