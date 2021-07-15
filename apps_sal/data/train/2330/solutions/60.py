S = input()
N = len(S)

if S[0] == '0' or S[-1] == '1' or S[:-1] != S[-2::-1]:
    print((-1))
    return

cur_node = 1
for i in range(N - 1):
    print((cur_node, i + 2))
    if S[i] == '1':
        cur_node = i + 2

