def convert(line):
    return "".join([chr(int(line[i:i + 2])) for i in range(0, len(line), 2)])
