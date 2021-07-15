def find_min_max_product(arr, k):
    n = len(arr)
    if (k>n):
        return None
    
    t_plus =[]
    t_minus = []
    res = []
    for to in arr:
        if (to==0):
            res.append(0)
        elif to>0:
            t_plus.append(to)
        else:
            t_minus.append(to)
            
    t_plus.sort()
    t_minus.sort()
    
    for to in t_plus:
        res.append(to)
    for to in t_minus:
        res.append(to)
    
    ans = 1
    
    for i in range(k):
        ans = ans*res[i];
        
    ans_min = ans
    ans_max = ans
    
    for i in range(n-k+1):
        ans = 1
        for j in range(i,i+k):
            ans=ans*res[j]
            
        ans_min = min(ans,ans_min)
        ans_max = max(ans,ans_max)
    
    
    return (ans_min,ans_max)

