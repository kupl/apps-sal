def find_all(sum_dig, digs):
    mn = float("inf")
    mx = -float("inf")
    def rec(i,sm,path):
        nonlocal mn,mx
        if i>=digs:
            if sum_dig==sm:
                num = int("".join(path))
                mn = min(mn,num)
                mx = max(mn,num)
                return 1
            else:
                return 0
        j = 1
        if path:
            j = int(path[-1])
        res = 0
        for k in range(j,10):
            res+=rec(i+1,sm+k,path+[str(k)])
        return res
    cnt = rec(0,0,[])
    if mn==float("inf") or mx==-float("inf"):
        return []
    return [cnt,mn,mx]
