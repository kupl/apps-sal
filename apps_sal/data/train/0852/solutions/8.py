t = int(input())

for i in range(t):
    k = int(input()) 
    ini = [j % 2 for j in range(0, k)]
    for j in range(0, k):
        print(''.join([str((x + j) % 2) for x in ini]))
