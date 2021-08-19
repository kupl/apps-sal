n = int(input())
ref = []
sums = []
for i in range(0, 10):
    ref.append([])
    for j in range(0, 10):
        ref[-1].append(int(list(str(i * j))[-1]))
    sums.append(sum(ref[-1]))
pref = []
for i in ref:
    pref.append([i[0]])
    for j in range(1, len(i)):
        pref[-1].append(pref[-1][-1] + i[j])
for i in range(0, n):
    ln = [int(j) for j in input().split(' ')]
    a = ln[0]
    b = ln[1]
    dig = int(list(str(b))[-1])
    ct = a // (b * 10)
    rem = a % (b * 10) // b
    print(ct * sums[dig] + pref[dig][rem])
