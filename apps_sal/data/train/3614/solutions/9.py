from collections import defaultdict

def interpreter(tape):
    mem, out = defaultdict(int), []

    n = len(tape)
    idx = ptr = 0
    while idx < n:
        cmd = tape[idx]

        if   cmd == '>': ptr += 1
        elif cmd == '<': ptr -= 1
        elif cmd == '+': mem[ptr] = (mem[ptr] + 1) % 256
        elif cmd == '-': mem[ptr] = (mem[ptr] - 1) % 256
        elif cmd == '/': mem[ptr] = 0
        elif cmd == '*': out.append(chr(mem[ptr]))

        idx += 1
    return ''.join(out)
