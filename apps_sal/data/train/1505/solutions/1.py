N = int(input())
s = input()
d = 0
md = 0
mdpos = 0
pl = 0
mpl = 0
plstart = 0
for i in range(N):
    t = s[i*2]
    if t == '1':
        d += 1
        if d > md :
            md = d
            mdpos = i
    else:
        d -= 1
    pl += 1
    if d == 0:
        if pl> mpl:
            mpl = pl
            mplstart = plstart
        plstart = i+1
        pl = 0
print(md,mdpos+1,mpl,mplstart+1)


