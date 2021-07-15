# cook your dish here
try:
    for _ in range(int(input())):
        class mat(object):
        	game=[]
        	limit=[]
        def see(key):
        	for i in range(len(mat.limit)-1,-1,-1):
        		if mat.limit[i]==key:
        			return False
        	return True
        def passes(n,m,arr):
        	if m>len(arr) or n>len(arr):
        		return
        	mat.game[n][m]+=1
        	mat.limit.append(m)
        	for i in range(1,arr[m]+1):
        		if m-i>0 and n<len(arr)-1 and not(m-i in mat.limit) :
        			passes(n+1,m-i,arr)
        		if m+i<len(arr)  and n<len(arr)-1 and not(m+i in mat.limit):
        			passes(n+1,m+i,arr)
        	mat.limit.pop()
        n=int(input())
        arr=list(map(int,input().split()))
        mat.game=[[0]*(len(arr)) for _ in range(len(arr))]
        passes(0,0,arr)
        ans=0
        for i in mat.game:
        	ans+=sum(i)
        print(ans)
        
except:
    pass
