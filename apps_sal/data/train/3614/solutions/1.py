def interpreter(tape):
    data, pointer, output = [0], 0, "",
    for command in tape:
        if   command == ">":
            pointer += 1
        elif command == "<":
            pointer -= 1
        elif command == "+" and is_valid(pointer, data):
            data[pointer] = (data[pointer] + 1) % 256
        elif command == "-" and is_valid(pointer, data):
            data[pointer] = (data[pointer] - 1) % 256
        elif command == "/" and is_valid(pointer, data):
            data[pointer] = 0
        elif command == "!":
            data.append(0)
        elif command == "*" and is_valid(pointer, data):
            output += chr(data[pointer])
        elif command == "*":
            output += chr(0)
    return output

def is_valid(pointer, data):
    return pointer >= 0 and pointer < len(data)
