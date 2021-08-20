t = int(input())
f = 0
y = 0
for _ in range(t):
    n = int(input())
    seq = [int(x) for x in input().split()]
    prev = seq[0]
    for i in range(1, len(seq)):
        if prev == seq[i]:
            seq[i] = 0
        prev = seq[i]
    ans = 0
    anss = 0
    for el in seq:
        if el != 0:
            c = seq.count(el)
            if ans < c:
                ans = c
                anss = el
            elif ans == c:
                if el < anss:
                    anss = el
                else:
                    anss = anss
    print(anss)
