from collections import defaultdict
import collections
def subarraysDivByK(A,K):
        d = collections.defaultdict(int)
        # generate accum
        accum = [0,]*len(A)
        for ai, a in enumerate(A): 
            div = a%K if ai == 0 else (a+accum[ai-1])%K
            accum[ai] = div; d[div] += 1 
        # count
        #print(accum,d)
        ans = 0
        for k,v in list(d.items()):
            ans +=  v*(v-1)//2
            if k == 0: ans += v 
        return ans
t=int(input())
for i in range(0,t):
      n=int(input())
      arr =  [int(x) for x in input().split()]   
      Sum = 1000000000
      print(subarraysDivByK(arr,Sum))  

  

