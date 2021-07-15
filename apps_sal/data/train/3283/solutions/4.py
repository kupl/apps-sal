def union_jack(n):
    try:
        n=-min(-7,int(-n//1))
    except:return False
    f=[['-X'[i==j or i==n-j-1 or (n-1)//2<=i<=n//2 or (n-1)//2<=j<=n//2]for i in range(n)]for j in range(n)]
    return'\n'.join(''.join(l)for l in f)
