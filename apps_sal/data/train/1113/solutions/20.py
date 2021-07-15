def main():
	no_tcase=int(input())
	for i in range(no_tcase):
		countdict={}
		no_ele=int(input())
		ls=[int(ele) for ele in input().split()]
		for ele in range(no_ele):
			if ls[ele] in countdict:
				countdict[ls[ele]]=countdict[ls[ele]]+1
			else:
				countdict[ls[ele]]=1
		maxk=ls[0]		
		maxval=countdict[maxk]
		for key in list(countdict.keys()):
			if countdict[key]>maxval:
				maxk=key
				maxval=countdict[key]
			elif countdict[key]==maxval and maxk>key:
				maxk=key
			else:
				continue
		print(maxk,maxval)
		
def __starting_point():
	main()

__starting_point()
