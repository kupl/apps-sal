def scrabble_score(st): 
    x = 0
    for y in st:
        if 'a' in y.lower():
            x += 1
        if 'e' in y.lower():
            x += 1
        if 'i' in y.lower():
            x += 1
        if 'o' in y.lower():
            x += 1
        if 'u' in y.lower():
            x += 1
        if 'l' in y.lower():
            x += 1
        if 'n' in y.lower():
            x += 1
        if 'r' in y.lower():
            x += 1
        if 's' in y.lower():
            x += 1
        if 't' in y.lower():
            x += 1
        if 'd' in y.lower():
            x += 2
        if 'g' in y.lower():
            x += 2
        if 'b' in y.lower():
            x += 3
        if 'c' in y.lower():
            x += 3
        if 'm' in y.lower():
            x += 3
        if 'p' in y.lower():
            x += 3
        if 'f' in y.lower():
            x += 4
        if 'h' in y.lower():
            x += 4
        if 'v' in y.lower():
            x += 4
        if 'w' in y.lower():
            x += 4
        if 'y' in y.lower():
            x += 4
        if 'k' in y.lower():
            x += 5
        if 'j' in y.lower():
            x += 8
        if 'x' in y.lower():
            x += 8
        if 'q' in y.lower():
            x += 10
        if 'z' in y.lower():
            x += 10
    return x
