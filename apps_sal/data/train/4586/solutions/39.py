def tv_remote(word):
    keyboard = ['abcde123', 'fghij456', 'klmno789', 'pqrst.@0', 'uvwxyz_/']
    x = 0
    y = 0
    steps = 0
    for c in word:
        while keyboard[y][x] != c:
            steps += 1
            print(keyboard[y][x])
            if c in keyboard[y]:
                if keyboard[y].find(c) < x:
                    x -= 1
                else:
                    x += 1
            elif ''.join(keyboard).find(c) < y * 8 + x:
                y -= 1
            else:
                y += 1
        steps += 1
    return steps
