import sys
blocks = {}
for i in range(1, 10):
    blocks[i] = [(0, 0)]
for i in range(2, 10, 2):
    for j in range(1, i / 2 + 1):
        blocks[i].append((j, 0))
        blocks[i + 1].append((0, j))
blocks[10] = [(0, 0), (0, 1), (1, 0), (1, 1)]
blocks[11] = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
blocks[12] = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]
blocks[13] = [(0, 2), (1, 2), (2, 0), (2, 1), (2, 2)]
blocks[14] = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
blocks[15] = [(0, 0), (0, 1), (0, 2), (1, 0), (2, 0)]
blocks[16] = [(0, 0), (0, 1), (1, 0)]
blocks[17] = [(0, 0), (0, 1), (1, 1)]
blocks[18] = [(0, 1), (1, 0), (1, 1)]
blocks[19] = [(0, 0), (1, 0), (1, 1)]
grid = [['.'] * 10] * 10
(id1, id2, id3) = list(map(int, input().split()))
while not id1 == id2 == id3 == -1:
    print('-1 -1 -1 -1 -1 -1 -1 -1 -1')
    sys.stdout.flush()
    (id1, id2, id3) = list(map(int, input().split()))
