def solve(a):
    r = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            curr_diff = a[-1]-a[0]+j-i
            if curr_diff%(len(a)-1) == 0:
                curr_a = [a[0]+i] + a[1:-1] + [a[-1]+j] 
                k = curr_diff//(len(a)-1)
                t = [abs(curr_a[0]+i*k-a[i]) for i in range(len(a))]  
                if max(t) <= 1: r.append(sum(t))
                    
    return min(r) if r else -1
