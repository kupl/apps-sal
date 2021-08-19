def reverse(s):
    (index, l) = (0, [[]])
    for x in s:
        if x in l[index]:
            l[index].append(x)
        elif not l[index]:
            l[index].append(x)
        else:
            l.append([x])
            index += 1
    return ''.join((''.join((c.swapcase() for c in x)) if len(x) > 1 else x.pop() for x in l))
