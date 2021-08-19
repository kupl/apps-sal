T = eval(input())
for i in range(T):
    N = eval(input())
    inp = input().split()
    linp = []
    for item in inp:
        linp.append(int(item))
    linp.sort()
    lout = []
    for i in range(N - 1):
        lout.append(linp[i + 1] - linp[i])
    print(min(lout))
