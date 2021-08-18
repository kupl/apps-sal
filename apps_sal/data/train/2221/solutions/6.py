from bisect import bisect_left

m = int(input())
lines = []
for i in range(m):
    lines.append(list(map(int, input().split())))
n = int(input())
lengths = list(map(int, input().split()))

acc_lengths = [0]
for l in lines:
    acc_lengths.append(acc_lengths[-1] + (1 if l[0] == 1 else l[1] * l[2]))

seq = []
for l in lines:
    if l[0] == 1:
        seq.append(l[1])
    else:
        for i in range(l[2]):
            seq.extend(seq[:l[1]])
            if len(seq) >= 10**5:
                break
    if len(seq) >= 10**5:
        break


def find_number(l):
    if l <= len(seq):
        return seq[l - 1]
    i = bisect_left(acc_lengths, l) - 1
    return seq[(l - acc_lengths[i] - 1) % lines[i][1]]


print(' '.join([str(find_number(l)) for l in lengths]))
