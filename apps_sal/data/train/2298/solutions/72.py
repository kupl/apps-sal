(n, t) = list(map(int, input().split()))
ar = list(map(int, input().split()))
mn = float('inf')
(mdif, mxc) = (-float('inf'), 0)
for e in ar:
    if e - mn > mdif:
        mdif = e - mn
        mxc = 1
    elif e - mn == mdif:
        mxc += 1
    mn = min(mn, e)
print(mxc)
