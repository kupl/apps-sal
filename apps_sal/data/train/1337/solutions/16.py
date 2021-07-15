# Python Program to find LCM of n elements 

def find_lcm(num1, num2): 
	if(num1>num2): 
		num = num1 
		den = num2 
	else: 
		num = num2 
		den = num1 
	rem = num % den 
	while(rem != 0): 
		num = den 
		den = rem 
		rem = num % den 
	gcd = den 
	lcm = int(int(num1 * num2)/int(gcd)) 
	return lcm 
for j in range(int(input())):
    n=int(input())
    l =list(map(int,input().split())) 
    x=int(input())
    num1 = l[0] 
    num2 = l[1] 
    lcm = find_lcm(num1, num2) 
    for i in range(2, len(l)):
        lcm = find_lcm(lcm, l[i])
    lcm+=x
    print(lcm)
	
 

# Code contributed by Mohit Gupta_OMG 

