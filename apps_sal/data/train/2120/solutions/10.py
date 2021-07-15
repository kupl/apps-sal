'''input
5
2 1
3
2 3
2 1
3
'''

from sys import stdin, setrecursionlimit

setrecursionlimit(15000)


# main starts
n = int(stdin.readline().strip())
arr = [0]
cur_sum = 0
aux = [0]
for _ in range(n):
	op = list(map(int, stdin.readline().split()))
	
	# processing operations
	if op[0] == 1:
		aux[op[1] - 1] += op[2]
		cur_sum += op[1] * op[2]

	elif op[0] == 2:
		aux.append(0)
		arr.append(op[1])
		cur_sum += op[1]		
	else:
		cur_sum -= (arr[-1] + aux[-1])
		aux[-2] += aux[-1]
		aux.pop()
		arr.pop()
	print(cur_sum / len(arr))
