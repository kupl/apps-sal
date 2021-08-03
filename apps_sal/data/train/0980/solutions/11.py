import sys


def lazy_jem(N_B_M):
    time_taken = 0
    while N_B_M[0] != 1:
        if(N_B_M[0] % 2 == 0):
            time_taken += ((N_B_M[0] / 2) * N_B_M[2])
            N_B_M[0] = N_B_M[0] - (N_B_M[0] / 2)
        else:
            time_taken += (((N_B_M[0] + 1) / 2) * N_B_M[2])
            N_B_M[0] = N_B_M[0] - ((N_B_M[0] + 1) / 2)
        N_B_M[2] = 2 * N_B_M[2]
        time_taken += N_B_M[1]
    time_taken += N_B_M[2]
    print(time_taken)


test_cases = eval(input())

for i in range(test_cases):
    N_B_M = list(map(int, input().strip().split(' ')))
    lazy_jem(N_B_M)
