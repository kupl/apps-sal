for t in range(0,int(input())):
  n=int(input())
  ss=list(map(str,input().split()))
  
  unique_words=set(ss)

  ans=""
  cnt=0

  for i in unique_words:
    if ss.count(i)>cnt :
      cnt=ss.count(i)
      ans=i
    elif ss.count(i)==cnt:
      if i < ans:
        ans=i
  
  print(ans)
