k = int(input())


edges = [['N' for i in range(1010)] for j in range(1010)]
vertices = 2


def add_edge(a, b):
    nonlocal edges
    edges[a][b] = edges[b][a] = 'Y'


for i in range(1, 29 + 1):
    vertices += 3
    add_edge(i * 3, i * 3 - 1)
    add_edge(i * 3, i * 3 + 2)
    add_edge(i * 3 + 1, i * 3 - 1)
    add_edge(i * 3 + 1, i * 3 + 2)


for bit in range(30):
    if (1 << bit) & k:
        lst = 1
        for i in range((29 - bit) * 2):
            vertices += 1
            add_edge(lst, vertices)
            lst = vertices
        add_edge(lst, 3 * bit + 2)

print(vertices)

if 0:
    for i in range(1, vertices + 1):
        print(i, ':', '\n\t', end='')
        for j in range(1, vertices + 1):
            if edges[i][j] == 'Y':
                print(j, end=' ')
        print('')
else:
    print('\n'.join(map(lambda x: ''.join(x[1:vertices + 1]), edges[1:vertices + 1])))
