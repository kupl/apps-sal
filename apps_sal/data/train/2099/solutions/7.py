maxn = 100000+10
ans = [0 for i in range(maxn)]
vis = [0 for i in range(maxn)]

s = input()
arr = s.split()
n = int(arr[0])
k = int(arr[1])

ans[0] = 1
cnt = k
for i in range(1, k+1):
    tmp = ans[i-1] + cnt
    if tmp > k+1 or vis[tmp]==1:
        tmp = ans[i-1]-cnt
    vis[tmp] = 1
    ans[i] = tmp
    cnt -= 1
print(1, end='')
for i in range(1,k+1):
    print('', ans[i], end='')
for i in range(k+1, n):
    print('', i+1, end='')
print()

 	    		 	  				  		  		   	 	
