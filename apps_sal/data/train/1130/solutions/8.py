# cook your dish here
import math as m
for i in range(int(input())):
    ND = input().split()
    N = int(ND[0])
    D = int(ND[1])
    risk = 0
    L = list(map(int, input().split()))
    if D == 1:
        print(N)
    else:
        for i in L:
            if i <= 9 or i >= 80:
                risk += 1
        print(m.ceil(risk / D) + m.ceil((N - risk) / D))
