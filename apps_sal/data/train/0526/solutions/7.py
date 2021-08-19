t = int(input())
while t:
    t -= 1
    string = input()
    l = len(string)
    temp = string[0]
    occ = 1
    pre = 0
    this = 0
    for i in range(1, l):
        if string[i] == temp:
            occ += 1
        else:
            if occ != 1:
                pre += occ * 8
                this += 40
            else:
                pre += 8
                this += 8
            occ = 1
            temp = string[i]
    if occ == 1:
        pre += 8
        this += 8
    else:
        pre += 8 * occ
        this += 40
    print(pre - this)
