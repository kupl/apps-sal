
# // Problem : List of Books
# // Contest : CodeChef - IARCS OPC Judge Problems
# // URL : https://www.codechef.com/IARCSJUD/problems/BOOKLIST
# // Memory Limit : 256 MB
# // Time Limit : 2000 ms
# // Powered by CP Editor (https://github.com/cpeditor/cpeditor)

n = int(input())
a = list(map(int,input().split()))
q = int(input())
for i in range(q):
	k = int(input())
	print(a[k-1])
	a.pop(k-1)
