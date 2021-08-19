def interpreter(tape):
    (memory, ptr, output) = ({0: 0}, 0, '')
    for command in tape:
        if command == '>':
            ptr += 1
        elif command == '<':
            ptr -= 1
        elif command == '+':
            if memory.get(ptr) != None:
                memory[ptr] = (memory[ptr] + 1) % 256
        elif command == '-':
            if memory.get(ptr) != None:
                memory[ptr] = (memory[ptr] - 1) % 256
        elif command == '/':
            if memory.get(ptr) != None:
                memory[ptr] = 0
        elif command == '!':
            memory[len(memory)] = 0
        elif command == '*':
            output += chr(memory.get(ptr, 0))
    return output
