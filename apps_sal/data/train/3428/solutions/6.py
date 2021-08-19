import re


def scanner(q):
    (bitseq, mask) = ([], [])
    for row in range(20, 8, -1):
        bitseq.append(q[row][20])
        mask.append((row + 20) % 2 == 0)
        bitseq.append(q[row][19])
        mask.append((row + 19) % 2 == 0)
    for row in range(9, 21, 1):
        bitseq.append(q[row][18])
        mask.append((row + 18) % 2 == 0)
        bitseq.append(q[row][17])
        mask.append((row + 17) % 2 == 0)
    for row in range(20, 8, -1):
        bitseq.append(q[row][16])
        mask.append((row + 16) % 2 == 0)
        bitseq.append(q[row][15])
        mask.append((row + 15) % 2 == 0)
    for row in range(9, 11, 1):
        bitseq.append(q[row][14])
        mask.append((row + 14) % 2 == 0)
        bitseq.append(q[row][13])
        mask.append((row + 13) % 2 == 0)
    code = [int(not x) if mask[i] else x for (i, x) in enumerate(bitseq)]
    length = int(''.join(map(str, code[4:12])), 2)
    return ''.join([chr(int(x, 2)) for x in re.findall('[01]{8}', ''.join(map(str, code[12:8 * length + 12])))])
