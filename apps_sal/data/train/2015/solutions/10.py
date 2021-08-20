T = int(input())
childs = []
for i in range(1, T + 1):
    child = list(map(int, input().split(' ')))
    child.insert(0, i)
    childs.append(child)
c_l = []
check = True
while check:
    at_o = childs.pop(0)
    c_l.append(at_o[0])
    for i in range(len(childs)):
        childs[i][3] -= at_o[1]
        at_o[1] -= 1
        if at_o[1] <= 0:
            break
    if len(childs) <= 0:
        break
    i = 0
    run = True
    while run:
        if childs[i][3] < 0:
            at_h = childs.pop(i)
            for j in range(i, len(childs)):
                childs[j][3] -= at_h[2]
            i -= 1
        i += 1
        if i > len(childs) - 1:
            run = False
    if len(childs) <= 0:
        check = False
print(len(c_l))
print(*c_l)
