def transpose(amount, tab):
    (stack, tab) = ([], list(map(list, tab)))
    for (n, col) in reversed(list(enumerate(zip(*tab)))):
        if any(map(str.isdigit, col)):
            stack.append(col)
        elif stack:
            frets = [''.join(r).strip('-') for r in zip(*reversed(stack))]
            frets = [fret and int(fret) + amount for fret in frets]
            if any((fret and (not 0 <= fret <= 22) for fret in frets)):
                return 'Out of frets!'
            frets = list(map(str, frets))
            pad = max(map(len, frets))
            for (row, fret) in zip(tab, frets):
                row[n + 1:n + 1 + len(stack)] = str(fret).ljust(pad, '-')
            stack.clear()
    return list(map(''.join, tab))
