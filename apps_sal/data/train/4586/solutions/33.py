def tv_remote(word):
    arrayz = ['abcde123', 'fghij456', 'klmno789', 'pqrst.@0', 'uvwxyz_/']
    steps = 0
    x = 0
    y = 0
    for letter in word:
        for row in arrayz:
            if letter in row:
                y1 = arrayz.index(row)
                x1 = row.find(letter)
                continue
        steps += abs(x - x1) + abs(y - y1) + 1
        (x, y) = (x1, y1)
    return steps
