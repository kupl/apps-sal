import sys
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    array = []
    for i in range(n):
        lista = []
        lista[:] = map(int, input().strip().split())
        array.append(lista)
    j = n - 1
    i = 0
    counter = 0
    for _ in range(n):
        if array[i][j] != i + j + 1:
            counter += 1
            if j > 0:
                j -= 1
            else:
                i -= 1
            (i, j) = (j, i)
        elif j > 0:
            j -= 1
        else:
            i -= 1
    print(counter)
