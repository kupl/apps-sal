def poohbear(s):
    st = []
    loops = []
    for (i, c) in enumerate(s):
        if c == 'W':
            st.append(i)
        elif c == 'E':
            loops.append((st.pop(), i))
    cells = [0]
    p = 0
    m = 0
    i = 0
    output = ''
    while i < len(s):
        c = s[i]
        if c == '+':
            cells[p] = (cells[p] + 1) % 256
        elif c == '-':
            cells[p] = (cells[p] - 1) % 256
        elif c == '>':
            p += 1
            if p == len(cells):
                cells.append(0)
        elif c == '<':
            if p == 0:
                cells.insert(0, 0)
            else:
                p -= 1
        elif c == 'c':
            m = cells[p]
        elif c == 'p':
            cells[p] = m
        elif c == 'W':
            if cells[p] == 0:
                for (w, e) in loops:
                    if i == w:
                        i = e
                        break
        elif c == 'E':
            if cells[p] != 0:
                for (w, e) in loops:
                    if i == e:
                        i = w
                        break
        elif c == 'P':
            output += chr(cells[p])
        elif c == 'N':
            output += str(cells[p])
        elif c == 'T':
            cells[p] = cells[p] * 2 % 256
        elif c == 'Q':
            cells[p] = cells[p] ** 2 % 256
        elif c == 'U':
            cells[p] = int(cells[p] ** 0.5) % 256
        elif c == 'L':
            cells[p] = (cells[p] + 2) % 256
        elif c == 'I':
            cells[p] = (cells[p] - 2) % 256
        elif c == 'V':
            cells[p] = cells[p] // 2 % 256
        elif c == 'A':
            cells[p] = (cells[p] + m) % 256
        elif c == 'B':
            cells[p] = (cells[p] - m) % 256
        elif c == 'Y':
            cells[p] = cells[p] * m % 256
        elif c == 'D':
            cells[p] = cells[p] // m % 256
        i += 1
    return output
