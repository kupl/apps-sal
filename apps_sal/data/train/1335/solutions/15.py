# cook your dish here
n=int(input())
lst=list(map(int,input().split()))
freq={}
for i in lst:
 if i not in freq:
  freq[i]=1 
 else:
  freq[i]+=1 
#print(freq)
day=0
for i in freq.values():
 if i%2==0:
  day=day+(i//2)
 else:
  day=day+(i//2)+1
  
print(day)
