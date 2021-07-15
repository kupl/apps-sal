t = int(input())

for i in range(t):
    k = int(input()) # 4
    ini = [x for x in range(1, k + 1)]
    for j in range(0, k):
        print("".join([str(x+1) for x in range(j*k, j*k + k)]))
