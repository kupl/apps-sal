t = int(input())
for i in range(t):
    k = int(input())
    ini = [x + 2 for x in range(0, k)]
    for j in range(0, k):
        print(''.join([str(x + j) for x in ini]))
