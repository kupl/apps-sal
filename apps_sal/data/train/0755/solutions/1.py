def find_gcd(x, y): 
	
	while(y): 
		x, y = y, x % y 
	
	return x 
		
def print_factors(x):
   for i in range(2, x + 1):
       if x % i == 0:
           print(i,end=" ")
t=int(input())
l=[]
for i in range(t):
    n=int(input())
    l.append(n)
l2=[]
i=0
for i in range(t-1):
    l2.append(abs(l[i+1]-l[i]))


num1 = l2[0] 
num2 = l2[1] 
gcd = find_gcd(num1, num2) 

for i in range(2, len(l2)): 
	gcd = find_gcd(gcd, l2[i]) 
	
#print(gcd) 
print_factors(gcd)



