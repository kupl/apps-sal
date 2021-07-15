def solve(a):
    ans,last = [],len(a)-1
    for i,x in enumerate(a):
        s = 'Begin' if i == last else 'Right' if a[i+1][0] == 'L' else 'Left'
        ans.insert(0,s + x[x.index(' '):])
    return ans
