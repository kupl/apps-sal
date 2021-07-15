N = int(input())
M = []
for i in range(N):
    x = int(input())
    M.append(x)
    M.sort()
    print(i+1-M.index(x))
