import sys

T = int(sys.stdin.readline())

while(T):
    T -= 1
    ins = sys.stdin.readline().split()
    R = int(ins[0])
    C = int(ins[1])
    horiwords = []
    vertiwords = [' '] * C
    flag = False
    for i in range(R):
        horiwords.append(sys.stdin.readline().lower())
        if 'spoon' in horiwords[i]:
            flag = True

    if not flag:
        for i in range(C):
            for j in range(R):
                vertiwords[i] += horiwords[j][i]
            if 'spoon' in vertiwords[i]:
                flag = True
                break

    if(flag):
        print('There is a spoon!')
    else:
        print('There is indeed no spoon!')
