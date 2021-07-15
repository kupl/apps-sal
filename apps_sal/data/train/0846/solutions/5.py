import sys
import math
#from queue import *
import random
#sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline
 
############ ---- USER DEFINED INPUT FUNCTIONS ---- ############
def inp():
    return(int(input()))
def inara():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(list(map(int,input().split())))
################################################################
############ ---- THE ACTUAL CODE STARTS BELOW ---- ############

k,a,b=invr()

if k<a-1:
	print(1+k)
	return

now=a
k-=(a-1)

if b-a>=3:
	now=a+(k//2)*(b-a)+k%2
else:
	now=a+k

print(now)
	
		

