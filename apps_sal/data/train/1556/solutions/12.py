t = int(input())
for i in range(t):
    k = int(input())
    ini = ''.join([str(i % 2) for i in range(1, k + 1)])
    for j in range(0, k):
        print(ini)
