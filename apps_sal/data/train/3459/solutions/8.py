def solve(n,k):
    s=''
    for i in str(n):
        if k==0:
            s+=i
        else:
            while s and s[-1]>i and k:
                k-=1
                s=s[:-1]   
            s+=i
            p=i
    return s[:-k] if k else s 
