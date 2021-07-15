import re

class memory(dict):
    def __init__(self, default):
        super().__init__()
        self._def = default
    def __getitem__(self, key): return self.get(key, self._def)

def poohbear(code):
    code, output = list(re.sub(r'[^+-><cpWEPNTQULIVABYD]', '', code)), []
    data, p, = memory(0), 0
    loop, ind, ins = [], 0, None
    copy_ = 0
    while ind < len(code):
        ins = code[ind]
        if ins == '+': data[p] = (data[p] + 1) % 256
        elif ins == '-': data[p] = (data[p] - 1) % 256
        elif ins == '<': p -= 1
        elif ins == '>': p += 1
        elif ins == 'c': copy_ = data[p]
        elif ins == 'p': data[p] = copy_
        elif ins == 'W':
            if data[p]: loop.append(ind)
            else:
                depth = 1
                while depth > 0:
                    ind += 1
                    c = code[ind]
                    if c == 'W': depth += 1
                    elif c== 'E': depth -= 1                
        elif ins == 'E':
            if data[p]: ind = loop[-1]
            else: loop.pop()
        elif ins == 'P': output.append(chr(data[p]))
        elif ins == 'N': output.append(str(data[p]))
        elif ins == 'T': data[p] = (data[p] * 2) % 256
        elif ins == 'Q': data[p] = (data[p] ** 2) % 256
        elif ins == 'U': data[p] = int(data[p] ** 0.5) % 256
        elif ins == 'L': data[p] = (data[p] + 2) % 256
        elif ins == 'I': data[p] = (data[p] - 2) % 256
        elif ins == 'V': data[p] = (data[p] // 2) % 256
        elif ins == 'A': data[p] = (data[p] + copy_) % 256
        elif ins == 'B': data[p] = (data[p] - copy_) % 256
        elif ins == 'Y': data[p] = (data[p] * copy_) % 256
        elif ins == 'D': data[p] = (data[p] // copy_) % 256
        ind += 1
    return ''.join(output)
