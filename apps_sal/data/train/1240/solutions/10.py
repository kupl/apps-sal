import sys 
from math import log2
from itertools import combinations 

#input = sys.stdin.readline
#sys.stdin.readline()
#sys.stdout.write("\n")

# #For getting input from input.txt file
# sys.stdin = open('Python_input1.txt', 'r')

# # Printing the Output to output.txt file
# sys.stdout = open('Python_output1.txt', 'w')



for _ in range(int(sys.stdin.readline())):
	n = int(sys.stdin.readline())
	lis  =list(map(int,sys.stdin.readline().split()))
	for i in range(len(lis)):
		if lis[i]%6 == 0:
			lis[i] = 6
		else:
			lis[i] = lis[i]%6
	#print(lis)
	print(sum(lis))
	

