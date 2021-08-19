t = int(input())
while t:
    A = input()
    B = input()
    mp1 = 0
    p1 = 0
    mp0 = 0
    p0 = 0
    for i in range(len(B)):
        if A[i] == B[i] and B[i] == '1':
            p1 += 1
        elif A[i] == B[i] and B[i] == '0':
            p0 += 1
        elif A[i] != B[i] and B[i] == '1':
            mp0 += 1
        else:
            mp1 += 1
    if mp0 + p0 == len(A) or mp1 + p1 == len(A):
        con = False
    elif mp1 + p0 >= mp0 + p0:
        con = True
        op = mp1 - mp0
        mp1 -= op
        op += mp1
    else:
        con = True
        op = mp0 - mp1
        mp0 -= op
        op += mp0
    if con:
        print('Lucky Chef')
        print(op)
    else:
        print('Unlucky Chef')
    t -= 1
