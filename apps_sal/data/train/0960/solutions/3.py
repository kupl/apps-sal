t = int(input())
for i in range(t):
    k = int(input())
    for j in range(0, k):
        print(' '.join([str(bin(x + 1)[2:]) for x in range(j * k, j * k + k)]))
