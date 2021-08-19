t = eval(input())
for p in range(t):
    line = input().split()
    (r, c) = (int(line[0]), int(line[1]))
    matrix = []
    found = False
    for i in range(r):
        matrix.append(input().lower())
    for i in range(r):
        if matrix[i].find('spoon') != -1:
            print('There is a spoon!')
            found = True
            break
    if not found:
        for i in range(c):
            line = ''
            for j in range(r):
                line += matrix[j][i]
            if line.find('spoon') != -1:
                print('There is a spoon!')
                found = True
                break
    if not found:
        print('There is indeed no spoon!')
