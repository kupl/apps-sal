# cook your dish here
T = int(input())

for _ in range(T):

    K = int(input())
    V = (K + 1) // 2

    for i in range(1, V + 1):
        line = ''
        for j in range(1, i + 1):
            if j == i:
                line = line + '*'
            else:
                line = line + ' '
        print(line)

    for i in range(V - 1, 0, -1):
        line = ''
        for j in range(1, i + 1):
            if j == i:
                line = line + '*'

            else:
                line = line + ' '

        print(line)
