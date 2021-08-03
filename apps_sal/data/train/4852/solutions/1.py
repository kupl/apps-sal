def interpreter(s):
    find, find_, d = [], [], {}
    for i, j in enumerate(s):
        if j == '[':
            find.append(i)
        if j == ']':
            find_.append(i)
    for i, j in zip(find, find_):
        d[i] = j
        d[j] = i
    memory, output, j = [0], [], 0
    while j < len(s):
        i = s[j]
        if i == "+":
            memory[-1] = (memory[-1] + 1) % 256
        if i == "-":
            memory[-1] = (memory[-1] - 1) % 256
        if i == '*':
            output.append(chr(memory[-1]))
        if i == "!":
            memory.append(0)
        if i == '[':
            if memory[-1] == 0:
                j = d[j]
        if i == "]":
            if memory[-1] != 0:
                j = d[j]
        if i == '^':
            memory.pop(-1)
        j += 1
    return "".join(output)
