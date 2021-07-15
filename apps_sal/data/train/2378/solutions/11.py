import sys
input = sys.stdin.readline

q=int(input())

from collections import Counter

for test in range(q):
    S=input().strip()

    C=Counter(S)

    L=C["L"]
    R=C["R"]
    U=C["U"]
    D=C["D"]

    if U==0 or D==0:
        if L>0 and R>0:
            print(2)
            print("LR")
            continue
        else:
            print(0)
            continue

    elif L==0 or R==0:
        if U>0 and D>0:
            print(2)
            print("UD")
            continue
        else:
            print(0)
            continue

    else:
        MU=min(U,D)
        ML=min(L,R)

        ANS="U"*MU+"R"*ML+"D"*MU+"L"*ML

        print(len(ANS))
        print(ANS)
        

    

