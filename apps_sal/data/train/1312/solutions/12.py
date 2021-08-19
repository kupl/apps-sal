cases = int(input())
for i in range(cases):
    (flag, lines) = (0, [])
    nums = input().split()
    (r, c) = (int(nums[0]), int(nums[1]))
    for j in range(r):
        lines.append(input().lower())
        if lines[j].find('spoon') >= 0:
            flag = 1
    for j in range(c):
        line = ''
        for k in range(r):
            line += lines[k][j]
        if line.find('spoon') >= 0:
            flag = 1
    if flag == 1:
        print('There is a spoon!')
    else:
        print('There is indeed no spoon!')
