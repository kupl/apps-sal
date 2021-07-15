# cook your dish here
def find_gcd(x, y): 
    while(y): 
        x, y = y, x % y 
  
    return x 


n,r = list(map(int, input().split()))
l = list(map(int, input().split()))
for i,ele in enumerate(l):
    if ele > 0:
        l[i] -= r
    else:
        l[i] += r
        

  
num1=l[0] 
num2=l[1] 
gcd=find_gcd(num1,num2) 
  
for i in range(2,len(l)): 
    gcd=find_gcd(gcd,l[i]) 
      
print(gcd) 

