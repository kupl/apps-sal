def string_constructing(a, s):
    current = ""
    step = 0
    while current != s:
        for i in range(len(current)):
            if i >= len(s):
                return step + len(current) - len(s)
            if current[i] != s[i]:
                current = current[i + 1:]
                s = s[i:]
                break
        else:
            current += a
        step += 1

    return step
