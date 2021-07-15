# cook your dish here
def find_gcd(x, y): 
    while(y): 
        x, y = y, x % y 
  
    return x 
      
n,r=list(map(int,input().split()))
l=list(map(int,input().split()))
b=[l[0]-r]
for i in range(n-1):
    b.append(l[i+1]-l[i])

num1=b[0]
num2=b[1]
gcd=find_gcd(num1,num2)
for j in range(2,len(b)):
    gcd=find_gcd(gcd,b[i])
print(gcd)
    

