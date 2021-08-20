"""z=int(input())
for i in range(z):
	n=int(input())
	counta=[]
	for i in range(1,n+1):
		count=0
		for j in range(1,i+1):
			if i%j==0:
				count+=1
		if count==2:
			counta.append(i)
	print(sum(counta)%10)
import math
n=int(input())
for i in range(n):
	m=int(input())
	summ=0
	for num in range(2,m+1):
	      	if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
	      		summ+=num
	print(summ%10)
import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n=int(input()) 
for i in range(n):
	m=int(input())
	summ=0
	for num in range(2,m+1):
	       	if is_prime(num):
	       		summ+=num 
	print(summ%10)"""


def sumOfPrimes(n):
    prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if prime[p] == True:
            i = p * 2
            while i <= n:
                prime[i] = False
                i += p
        p += 1
    sum = 0
    for i in range(2, n + 1):
        if prime[i]:
            sum += i
    return sum


t = int(input())
for i in range(t):
    n = int(input())
    print(sumOfPrimes(n) % 10)
