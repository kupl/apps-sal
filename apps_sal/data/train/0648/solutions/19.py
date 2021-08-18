inpt = list(map(int, input().split()))
n = inpt[0]
q = inpt[1]

h = list(map(int, input().split()))
for i in range(0, q):
    flag = 1
    oper = list(map(int, input().split()))
    typ = oper[0]
    if(typ == 2):
        for j in range(oper[1] - 1, oper[2]):
            h[j] = h[j] + oper[3]
    elif(typ == 1):
        start = oper[1] - 1
        pos = start
        jump = oper[2]
        count = 0
        jp = 0
        for l in range(pos + 1, n):
            count = count + 1
            if(jp == jump):
                break
            if(count > 100):
                break
            if(h[l] > h[pos]):
                start = l
                pos = start
                jp = jp + 1
                count = 0

        print(start + 1)
