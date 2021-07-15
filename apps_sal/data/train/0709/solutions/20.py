from sys import stdin,stdout                           #
import math                                            #
import heapq                                           #
                                                       #
t = 1                                                  #
def aint():                                            #
	return int(input().strip())                        #
def lint():                                            #
	return list(map(int,input().split()))              #
def fint():                                            #
	return list(map(int,stdin.readline().split()))     #
                                                       #	
########################################################
 
def main():
	n=aint()
	l=lint()
	pre=[l[0]]
	suff=[l[-1]]
	for i in range(1,n):
		pre.append(math.gcd(pre[-1],l[i]))
	for i in range(n-2,-1,-1):
		suff.append(math.gcd(suff[-1],l[i]))
	print(max(max(pre),max(suff)))
t=aint()
########################################################
for i in range(t):                                     #
	main()                                             #
