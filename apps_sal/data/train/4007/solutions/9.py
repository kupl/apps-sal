def finding_k(arr):
    ans=[]
    for i in range(1,101):
        if len({j%i for j in arr})==1:
            ans.append(i)
    return max(ans) if len(ans)<100 else -1
