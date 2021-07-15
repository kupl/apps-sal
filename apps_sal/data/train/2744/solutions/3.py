from collections import defaultdict

def poohbear(code):
    out, jumps, mem = [], {}, defaultdict(int)

    for i, c in enumerate(code):
        if   c == 'W': out.append(i)
        elif c == 'E': j = out.pop(); jumps[j], jumps[i] = i, j

    idx, ptr, c, n = 0, 0, 0, len(code)

    while idx < n:
        cmd = code[idx]

        if   cmd == '>': ptr       +=   1
        elif cmd == '<': ptr       -=   1
        elif cmd == '+': mem[ptr]  +=   1
        elif cmd == '-': mem[ptr]  -=   1
        elif cmd == 'L': mem[ptr]  +=   2
        elif cmd == 'I': mem[ptr]  -=   2
        elif cmd == 'T': mem[ptr]  *=   2
        elif cmd == 'V': mem[ptr] //=   2
        elif cmd == 'Q': mem[ptr] **=   2
        elif cmd == 'U': mem[ptr] **=  .5
        elif cmd == 'p': mem[ptr]   =   c
        elif cmd == 'A': mem[ptr]  +=   c
        elif cmd == 'B': mem[ptr]  -=   c
        elif cmd == 'Y': mem[ptr]  *=   c
        elif cmd == 'D': mem[ptr] //=   c
        elif cmd == 'c': c          =   mem[ptr]
        elif cmd == 'P': out.append(chr(mem[ptr]))
        elif cmd == 'N': out.append(str(mem[ptr])) 
        elif cmd == 'W' and not mem[ptr] or cmd == 'E' and mem[ptr]: idx = jumps[idx]

        mem[ptr] = round(mem[ptr]) % 256
        idx += 1
    return ''.join(out)
