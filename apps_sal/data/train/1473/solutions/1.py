import string
T = eval(input())
for x in range(T):
    b = input().split()
    R = int(b[0])
    C = int(b[1])
    M = int(b[2])
    K = int(b[3])
    J = int(b[4])
    if R * C != M + K + J:
        print('No')
        continue
    if R == 1 or C == 1:
        print('Yes')
        continue
    if M % R == 0:
        C = C - M / R
        if K % R == 0 or K % C == 0 or J % R == 0 or (J % C == 0):
            print('Yes')
            continue
        else:
            C = C + M / R
    if M % C == 0:
        R = R - M / C
        if K % R == 0 or K % C == 0 or J % R == 0 or (J % C == 0):
            print('Yes')
            continue
        else:
            R = R + M / C
    if K % R == 0:
        C = C - K / R
        if M % R == 0 or M % C == 0 or J % R == 0 or (J % C == 0):
            print('Yes')
            continue
        else:
            C = C + K / R
    if K % C == 0:
        R = R - K / C
        if M % R == 0 or M % C == 0 or J % R == 0 or (J % C == 0):
            print('Yes')
            continue
        else:
            R = R + K / C
    if J % R == 0:
        C = C - J / R
        if K % R == 0 or K % C == 0 or M % R == 0 or (M % C == 0):
            print('Yes')
            continue
        C = C + J / R
    if J % C == 0:
        R = R - J / C
        if K % R == 0 or K % C == 0 or M % R == 0 or (M % C == 0):
            print('Yes')
            continue
        else:
            R = R + J / C
    print('No')
