def pattern(n):
    if n<=0:
        return ""
    ans="1"
    for i in range(1,n):
        ans=ans+  "\n"+str(i+1)*(i+1)
    return ans
