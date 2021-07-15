# f = open('test.py')
# def input():
# 	return f.readline().replace('\n','')


from collections import defaultdict
import bisect
# from collections import deque

def read_list():
	return list(map(int,input().strip().split(' ')))
def print_list(l):
	print(' '.join(map(str,l)))


N = int(input())
for _ in range(N):
	n = int(input())
	nums = read_list()
	dic = defaultdict(list)
	for i in range(n):
		dic[nums[i]].append(i)
	data = list(set(nums))
	data.sort()
	l = len(data)
	res = 0
	if l>1:
		ind = bisect.bisect_left(dic[data[0]],dic[data[1]][0])
		ln = len(dic[data[1]])
		for j in range(len(dic[data[0]])-1,ind-1,-1):
			res = max(res,j+1+ln-bisect.bisect_left(dic[data[1]],dic[data[0]][j]))
		tmp = ind+ln
	else:
		tmp = 0
	for i in range(2,l):
		if dic[data[i]][0]>dic[data[i-1]][-1]:
			tmp+=len(dic[data[i]])
		else:
			res = max(res,tmp+len(dic[data[i]])-bisect.bisect_left(dic[data[i]],dic[data[i-1]][-1]))
			ind = bisect.bisect_left(dic[data[i-1]],dic[data[i]][0])
			ln = len(dic[data[i]])
			for j in range(len(dic[data[i-1]])-1,ind-1,-1):
				res = max(res,j+1+ln-bisect.bisect_left(dic[data[i]],dic[data[i-1]][j]))
			tmp = ind+ln
	res = max(res,tmp)
	for a in list(dic.values()):
		res = max(len(a),res)
	print(n-res)

