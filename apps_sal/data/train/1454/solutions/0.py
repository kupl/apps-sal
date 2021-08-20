import numpy as np
N = 10 ** 6 + 1
t = eval(input())
inp = ()
t1 = ord('z')
bag = np.zeros((N + 1, t1), dtype=np.int)
while t:
    t -= 1
    inp = input().split()
    t2 = ord(inp[3]) - ord('a')
    t3 = int(inp[1])
    t4 = int(inp[2]) + 1
    if inp[0] == '1':
        bag[t3][t2] += int(inp[2])
    if inp[0] == '2':
        sum = 0
        for i in range(t3, t4):
            sum += bag[i][t2]
        print(sum)
