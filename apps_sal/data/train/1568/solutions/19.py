T = int(input())
for i in range(T):
    N = int(input())
    S = input()
    S = S.split()
    cntr = 0
    for j in S:
        if int(j) >= N / 2:
            cntr += 1
    print(cntr)
