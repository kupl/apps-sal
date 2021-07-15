# def countSubStr(st,n):
# 	res = 0
# 	for i in range(0,n):
# 		if (st[i] == '1'):
# 			for j in range(i+1, n) :
# 				if (st[j] == '0'):
# 					res += 1
# 		if (st[i] == '0'):
# 			for j in range(i+1, n):
# 				if(st[j] == '1'):
# 					res += 1
# 	return res 
# for _ in range(int(input())):
# 	N = int(input());binstr = input()
# 	#for any N, number of contigious subarrays will be sum of all i in range(1,N + 1)
# 	print(countSubStr(list(binstr),N),end="") #TLE (obviously, since it's O(N**2))
for _ in range(int(input())):
	N = int(input());binstr = input()
	print(binstr.count('1')*binstr.count('0'))
