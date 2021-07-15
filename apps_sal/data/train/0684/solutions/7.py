# your code goes here
import math
def isp(n):
	m=2
	p=int(math.sqrt(n));
	while m<=p:
		if(n%m==0):
			break
		m+=1
	return p<m
t=int(input())
while t>0:
	n=int(input())
	if n==1:
	    print("Grinch")
	elif n==2 or n%2==1:
	    print("Me")
	else:
		m=0
		while n%2==0:
			m+=1
			n//=2
		if n==1:
			print("Grinch")
		elif m==1 and isp(n):
			print("Grinch")
		else:
			print("Me")
	t-=1
	        
	            
	            
	        

