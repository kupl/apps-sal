import sys
import queue

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def main():
	#a = int(input())
	n, m = tin()
	#s = input()
	al = [-1]+lin()
	bb=[[] for _ in range(n+1)]
	for _ in range(m):
		a, b = tin()
		bb[a].append(b)
		bb[b].append(a)
		
	ll=[]
	is_open = [0] *(n+1)
	for i in range(n+1):
		q=queue.Queue()
		q.put(i)
		t=[]
		while not q.empty():
			pp=q.get()
			if is_open[pp] != 0:
				continue
			is_open[pp]=1
			t.append(pp)
			for v in bb[pp]:
				q.put(v)
		ll.append(t)
	
	ret = 0
	#pa(ll)
	for t in ll:
		st=set(t)
		for v in t:
			if al[v] in st:
				ret += 1
	print(ret)
				
		
		
	
	
	
	
	
#+++++
isTest=False

def pa(v):
	if isTest:
		print(v)
		
def input_clipboard():
	import clipboard
	input_text=clipboard.get()
	input_l=input_text.splitlines()
	for l in input_l:
		yield l

def __starting_point():
	if sys.platform =='ios':
		if input_method==input_methods[0]:
			ic=input_clipboard()
			input = lambda : ic.__next__()
		elif input_method==input_methods[1]:
			sys.stdin=open('inputFile.txt')
		else:
			pass
		isTest=True
	else:
		pass
		#input = sys.stdin.readline
			
	ret = main()
	if ret is not None:
		print(ret)
__starting_point()
