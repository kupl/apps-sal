from string import ascii_lowercase
from bisect import bisect


def solve(s):
    pos = [[] for _ in range(26)]
    offset = ord('a')
    for (i, c) in enumerate(s):
        c = ord(c) - offset
        pos[c].append(i)
    for l in pos:
        l.append(len(s))
    all_char_sequence_start_pos = []
    pos_i = [len(l) - 1 for l in pos]
    while all((pi >= 0 for pi in pos_i)):
        i = min((l[pi] for (pi, l) in zip(pos_i, pos)))
        all_char_sequence_start_pos.append(i)
        for j in range(26):
            while pos_i[j] >= 0 and pos[j][pos_i[j]] >= i:
                pos_i[j] -= 1
    all_char_sequence_start_pos.reverse()
    ans = []
    curr = -1
    for i in all_char_sequence_start_pos:
        for c in range(26):
            cj = bisect(pos[c], curr)
            j = pos[c][cj]
            if j >= i:
                ans.append(c)
                curr = j
                break
    return ''.join((chr(c + offset) for c in ans))


print(solve(input().strip()))
