

def findMaximumNum(st, n, k): 
  
    for i in range(n):  
  
        if (k < 1):  
            break
  
        if (st[i] != '9'):  
  
            st = st[0:i] + '9' + st[i + 1:]  
  
             
            k -= 1
  
    return st 
  

st,k = input().split()
n = len(st)  
k = int(k)
print(findMaximumNum(st, n, k)) 
