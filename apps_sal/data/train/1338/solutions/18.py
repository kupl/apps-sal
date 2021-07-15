# cook your dish here
l=list(input().split())
for i in range(1,len(l),2):
	print("{0:.2f}".format(float(l[i])*10**float(l[i+1])))
