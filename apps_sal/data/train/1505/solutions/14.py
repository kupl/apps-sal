# cook your dish here
n = int(input())
l = input().split()

ml = []
mnd, mndi = -1, -1
c = 1
maxc, maxci = 0, 0
for i in range(n):
    if l[i] == '1':
        ml.append('1')
        if len(ml) > mnd:
            mnd = len(ml)
            mndi = i
    if l[i] == '2':
        ml.pop()
        if ml == []:
            if c > maxc:
                maxc = c
                maxci = i
            c = 0
    c += 1
if c > maxc:
    maxc = c
    maxci = i
print(mnd, mndi + 1, maxc, maxci - maxc + 2)
