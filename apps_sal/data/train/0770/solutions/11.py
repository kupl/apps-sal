T = int(input())

while(T > 0):
    N, K = list(map(int, input().split()))
    A = [int(e) for e in input().split()]

    E = [0] * N
    LE = -1
    LO = -1
    O = [0] * N

    if(A[0] % 2 == 0):
        E[0] = A[0]
        LE = 0
    else:
        O[0] = A[0]
        LO = 0

    i = 1
    while(i < N):

        if(A[i] % 2 == 0):
            O[i] = O[i - 1]
            if(LE != -1):
                if(abs(i - LE) <= K):
                    if((i - K - 1) >= 0):
                        ADDI = E[i - K - 1]
                    else:
                        ADDI = 0

                    if(E[LE] >= A[i] + ADDI):
                        E[i] = E[LE]
                        LE = LE
                    else:
                        E[i] = A[i] + ADDI
                        LE = i
                else:
                    E[i] = E[LE] + A[i]
                    LE = i

            else:
                E[i] = E[i - 1] + A[i]
                LE = i
        else:
            E[i] = E[i - 1]

            if(LO != -1):

                if(abs(i - LO) <= K):
                    if((i - K - 1) >= 0):
                        ADDI = O[i - K - 1]
                    else:
                        ADDI = 0

                    if(O[LO] >= A[i] + ADDI):
                        O[i] = O[LO]
                        LO = LO
                    else:

                        O[i] = A[i] + ADDI
                        LO = i
                else:
                    O[i] = O[LO] + A[i]
                    LO = i

            else:
                O[i] = O[i - 1] + A[i]
                LO = i

        i = i + 1

    print(E[N - 1] + O[N - 1])
    T = T - 1
