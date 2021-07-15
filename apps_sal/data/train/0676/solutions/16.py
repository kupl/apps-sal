for t in range(0,int(input())):
  n=int(input())
  ss=list(map(str,input().split()))
  
  my_dict={}
  
  for i in ss:
    my_dict[i]=ss.count(i)

  ans=""
  cnt=0

  for key,value in my_dict.items():
    if value > cnt:
      cnt=value
      ans=key
    elif value==cnt:
      if key < ans:
        ans=key

        
  print(ans)
