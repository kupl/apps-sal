t=input()
arr=input().split()
arr=[int(i) for i in arr]
c=0
if len(arr)==t:
 for i in range(0,t):
	 for j in range(i,t):
		 c+=abs(arr[i]-arr[j])
 print(c)
