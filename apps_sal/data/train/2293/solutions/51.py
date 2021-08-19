import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
Max = [[(0, A[0])]]
ans = 0
for bit in range(1, 1 << N):
    dic = {bit: A[bit]}
    for i in range(N):
        if bit & 1 << i != 0:
            for (ind, val) in Max[bit - (1 << i)]:
                dic[ind] = val
    com = []
    for (ind, val) in dic.items():
        if len(com) < 2:
            com.append((ind, val))
        elif com[0][1] < com[1][1]:
            if com[0][1] < val:
                com[0] = (ind, val)
            elif com[1][1] < val:
                com[1] = (ind, val)
        elif com[1][1] < val:
            com[1] = (ind, val)
        elif com[0][1] < val:
            com[0] = (ind, val)
    Max.append(com)
    tmp = com[0][1] + com[1][1]
    if tmp > ans:
        ans = tmp
    print(ans)
