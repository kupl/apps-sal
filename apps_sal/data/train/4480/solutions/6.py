def parse(data):
    result = []
    value = 0
    for command in data:
        if command == 'i':
            value += 1
        elif command == 'd':
            value -= 1
        elif command == 's':
            value = value ** 2
        elif command == 'o':
            result.append(value)
    return result
