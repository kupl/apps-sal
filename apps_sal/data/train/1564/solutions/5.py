import sys

def work():

	j=eval(input())
	for k in range(j):
		s=input()
		a=''
		count=0
		for i in range(1,len(s)):
			s1=s[i-1]+s[i]
			if a.find(s1) == -1:
				a=a+s1
				count+=1
#				print a.find(s1)
#				print s1
#				print a
		print(count)

def main():
	work()


def __starting_point():
	main()
__starting_point()
