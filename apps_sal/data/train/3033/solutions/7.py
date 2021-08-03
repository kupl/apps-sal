def interpreter(s):
    d, output, p = [0], [], 0
    for i in s:
        if i == "+":
            d[p] += 1
        elif i == "*":
            output.append(chr(d[p]))
        elif i == ">":
            d.append(0)
            p += 1
        elif i == "<":
            if p == 0:
                d.insert(0, 0)
                p = 1
            p -= 1
    return "".join(output)
