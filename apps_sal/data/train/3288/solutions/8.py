def solve(st,k):
    return max([int(st[i:len(st)-k+i]) for i in range(0, k+1)])
