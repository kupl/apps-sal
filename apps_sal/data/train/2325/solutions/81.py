import numpy as np

S = list(input())
T = list(input())

count_A_S = np.r_[[0], np.array(S) == 'A']
count_A_S = count_A_S.cumsum()
count_B_S = np.r_[[0], np.array(S) == 'B']
count_B_S = count_B_S.cumsum()
count_A_T = np.r_[[0], np.array(T) == 'A']
count_A_T = count_A_T.cumsum()
count_B_T = np.r_[[0], np.array(T) == 'B']
count_B_T = count_B_T.cumsum()


def check(a1, b1, a2, b2):
    if a1 < a2:
        if b1 < b2:
            diff1 = a2 - a1
            diff2 = b2 - b1
            diff = abs(diff1 - diff2)
        else:
            diff = b1 - b2 + a2 - a1
    else:
        if b1 < b2:
            diff = a1 - a2 + b2 - b1
        else:
            diff1 = a1 - a2
            diff2 = b1 - b2
            diff = abs(diff1 - diff2)
    if diff % 3 == 0:
        return 'YES'
    else:
        return 'NO'


q = int(input())
ans = []
for i in range(q):
    a, b, c, d = map(int, input().split())
    num_a_s = count_A_S[b] - count_A_S[a - 1]
    num_b_s = count_B_S[b] - count_B_S[a - 1]
    num_a_t = count_A_T[d] - count_A_T[c - 1]
    num_b_t = count_B_T[d] - count_B_T[c - 1]
    ans.append(check(num_a_s, num_b_s, num_a_t, num_b_t))

print(*ans, sep='\n')
