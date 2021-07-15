def interpreter(tape):
    memory, ptr, output = {}, 0, ""
    
    for command in tape:
        if   command == ">":  ptr += 1
        elif command == "<":  ptr -= 1
        elif command == "+":  memory[ptr] = (memory.get(ptr, 0) + 1) % 256
        elif command == "*":  output += chr(memory[ptr])
    
    return output
