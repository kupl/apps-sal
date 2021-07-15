'''
    ssisodia507@gmail.com
'''


def solve(array,k,n):
 
 # storing even and odd values
 even=[]
 odd=[]
 for i in range(n):
  if array[i]%2==0:
   even.append(array[i])
   odd.append(0)
  else:
   odd.append(array[i])
   even.append(0)
 
 # dpEven will store the maximum sum of even elements till index i-th
 # and dpOdd of odd elements till index i-th
 dpEven=[0]*n
 dpOdd=[0]*n
 dpEven[0]=even[0]
 dpOdd[0]=odd[0]
 
 # from index 0 to k we can only select one even value and one odd value
 # so store the maximum even value till index k and maximum odd value 
 # till index k
 i=1
 while i<=k and i<n:
  dpEven[i]=max(dpEven[i-1],even[i])
  dpOdd[i]=max(dpOdd[i-1],odd[i])
  i+=1
 
 # now for any element we have two choices
 # either choose it or leave it.
 
 # we will consider the case which will give maximum sum
 # so we will find the sum after leaving the element(which is previous
 # maximum sum ) and after choosing the element(previous sum+currentvalue) 
 # and pick the one which give maximum sum
 
 # we will handle even and odd cases separately 
 for i in range(k+1,n):
  dpEven[i]=max(dpEven[i-1],dpEven[i-k-1]+even[i])
 for i in range(k+1,n):
  dpOdd[i]=max(dpOdd[i-1],dpOdd[i-k-1]+odd[i])
 return dpOdd[-1]+dpEven[-1]
queries=[]
for _ in range(int(input())):
 n,k=map(int,input().split( ))
 queries.append((list(map(int,input().split( ))),k))

for query in queries:
 print(solve(query[0],query[1],len(query[0])))
