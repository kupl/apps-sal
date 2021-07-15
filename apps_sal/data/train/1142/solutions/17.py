# 
# // Problem : Whats the Rank
# // Contest : CodeChef - IARCS OPC Judge Problems
# // URL : https://www.codechef.com/IARCSJUD/problems/IARANK
# // Memory Limit : 256 MB
# // Time Limit : 2000 ms
# // Powered by CP Editor (https://github.com/cpeditor/cpeditor)

res = []
for _ in range(int(input())):
	n = int(input())
	res.append(n)
	res.sort(reverse=True)
	print(res.index(n)+1)
