import collections

def CountFrequency(arr): 
    return collections.Counter(arr)


for t in range(0,int(input())):
  n=int(input())
  arr=list(map(str,input().split()))

  freq=CountFrequency(arr)
  
  ans=""
  cnt=0

  for key,value in freq.items():
    if value > cnt:
      cnt=value
      ans=key
    elif value==cnt:
      if key < ans:
        ans=key


  print(ans)
