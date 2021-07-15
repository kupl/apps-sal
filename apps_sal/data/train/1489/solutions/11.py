# cook your dish here
n,k = map(int, input().split())
n = str(n)
for i in range(len(n)):
    if(k == 0):
        break
    if(n[i]!='9'):
        n = n[:i]+'9'+n[i+1:]
        k-=1
    
print(n)
