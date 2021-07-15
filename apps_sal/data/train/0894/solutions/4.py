import random
t=int(input())
for testCase in range(t):
	n=int(input())
	array1=[]
	array2=[]
	array=[]
	for i in range(n) :
		array1.append(list(map(int,input().split())))
	for i in range(n) :
		array2.append(list(map(int,input().split())))
	for i in range(n) :
		array.append(i)
#	print array2,"     ",array1
	for i in range(n) :
		print(array[i]+1, end=' ') 
	print() 
	k=0
	max=0
	answer=[]
	temp=[]
	while k < (1<<5) :
		k+=1	
		for i in range(n) :
			rand=random.randint(0,len(array)-1)
			temp.append(array[rand])
			array.pop(rand)
		array = temp
		count=0
		for i in range(n) :
			for j in range(n) :
				if(array1[i][j] and array2[array[i]][array[j]]) :
					count+=1
		if(count > max):
			answer=array
			max=count
			#print max,count
	for x in answer :
		print(x+1, end=' ')
	print()
