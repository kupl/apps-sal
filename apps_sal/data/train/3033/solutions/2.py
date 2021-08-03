from collections import defaultdict


def interpreter(tape):
    mem, p_mem, output = defaultdict(lambda: 0), 0, []
    for command in tape:
        if command == '>':
            p_mem += 1
        elif command == '<':
            p_mem -= 1
        elif command == '+':
            mem[p_mem] = mem[p_mem] + 1 & 0xff
        elif command == '*':
            output.append(mem[p_mem])
    return ''.join(map(chr, output))
