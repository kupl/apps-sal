for _ in range(int(input())):
    inp = input()
    count = 0
    for i in inp:
        if i != 'a' or i != 'e' or i != 'i' or (i != 'o') or (i != 'u'):
            if i == 'b' or i == 'd' or i == 'f' or (i == 'h') or (i == 'j') or (i == 'n') or (i == 'p') or (i == 't') or (i == 'v'):
                count += 1
            if i == 'c' or i == 'g' or i == 'k' or (i == 'm') or (i == 'q') or (i == 's') or (i == 'w'):
                count += 2
            if i == 'l' or i == 'r' or i == 'x':
                count += 3
            if i == 'y':
                count += 4
            if i == 'z':
                count += 5
    print(count)
