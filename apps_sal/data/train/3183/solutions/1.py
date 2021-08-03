def interpreter(tape):
    memory, ptr, output, skip, i = {0: 0}, 0, "", False, 0

    while True:
        command = tape[i]
        i = (i + 1) % len(tape)

        if command in "><+-*&/\\" and skip:
            skip = False
            continue

        if command == ">":
            ptr += 1
        elif command == "<":
            ptr -= 1
        elif command == "+":
            memory[ptr] = (memory.get(ptr, 0) + 1) % 256
        elif command == "-":
            memory[ptr] = (memory.get(ptr, 0) - 1) % 256
        elif command == "*":
            output += chr(memory.get(ptr, 0))
        elif command == "&":
            break
        elif command == "/" and memory[ptr] == 0:
            skip = True
        elif command == "\\" and memory[ptr] != 0:
            skip = True

    return output
