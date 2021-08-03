def interpreter(tape):
    j, k = {}, []
    for i in range(len(tape)):
        if tape[i] == "[":
            k.append(i)
        elif tape[i] == "]":
            j[i] = k[-1]
            j[k.pop()] = i

    m, r, i, l = [0], "", 0, len(tape)
    while i < l:
        if tape[i] == "^":
            m.pop(0)
        elif tape[i] == "!":
            m.append(0)
        elif tape[i] == "+":
            m[-1] += 1
        elif tape[i] == "-":
            m[-1] -= 1
        elif tape[i] == "*":
            r += chr(m.pop(0) % 256)
        elif (tape[i] == "[" and not m[-1] % 256) or (tape[i] == "]" and m[-1] % 256):
            i = j[i]
        i += 1
    return r
