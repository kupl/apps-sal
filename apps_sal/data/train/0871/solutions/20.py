import math

def nCr(n):
    f = math.factorial
    return f(n) // f(2) // f(n-2)
# Python3 program to count of index pairs 
# with equal elements in an array. 
import math as mt 

# Return the number of pairs with 
# equal values. 
def countPairs(arr, n): 

	mp = dict() 

	# Finding frequency of each number. 
	for i in range(n): 
		if arr[i] in mp.keys(): 
			mp[arr[i]] += 1
		else: 
			mp[arr[i]] = 1
			
	# Calculating pairs of each value. 
	ans = 0
	for it in mp: 
		count = mp[it] 
		ans += (count * (count - 1)) // 2
	return ans 

# cook your dish here
for _ in range(int(input())):
    (r,c)= map(int,input().split())
    has = []
    simple = []
    for i in range(r):
        lis = input()
        lis = list(lis)
        for j in range(c):
            if(lis[j]=='#'):
                has.append([i,j])
            elif(lis[j]!='-'):
                simple.append([lis[j],[i,j]])
    sum1=0
    for j in range(max(r,c)):
        he ,del1= [],[]
        flag = 0
        for i in simple:
            if(i[0]=='R' and i[1][1]+j+1<=c):
                if(has.count([i[1][0],i[1][1]+j+1])==0):
                    he.append((i[1][0],i[1][1]+j+1))
                else:
                    del1.append(i)
            elif(i[0]=='D' and i[1][0]+j+1<=r):
                if(has.count([i[1][0]+j+1,i[1][1]])==0):
                    he.append((i[1][0]+j+1,i[1][1]))
                else:
                    del1.append(i)
                    
            elif(i[0]=='L' and i[1][1]-j-1>=0):
                if(has.count([i[1][0],i[1][1]-j-1])==0):
                    he.append((i[1][0],i[1][1]-j-1))
                else:
                    del1.append(i)
                    
            elif(i[0]=='U' and (i[1][0]-j-1)>=0):
                if(has.count([i[1][0]-j-1,i[1][1]])==0):
                    he.append((i[1][0]-j-1,i[1][1]))
                else:
                   del1.append(i)
        sum1+=countPairs(he,len(he))
        for p in del1:
            simple.remove(p)
    print(sum1)
