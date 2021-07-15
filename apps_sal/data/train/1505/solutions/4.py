n = int(input())
seq = list(map(lambda x: 1 if x=="1" else -1, input().split()))
sums = [seq[0]]
for i in seq[1:]:
    sums.append(sums[-1]+i)
fin_pos = -1
pos = -1
counter = -1
m = -1
for i in range(n):
    v = sums[i]
    if counter == -1 and v == 1:
        counter = 0
        pos = i
    elif v == 0:
        if counter > m:
            m = counter
            fin_pos = pos
        counter = -1
    elif counter != -1:
        counter += 1

print(max(sums), sums.index(max(sums))+1, m + 2, fin_pos+1)
