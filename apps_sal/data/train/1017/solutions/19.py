for _ in range(int(input())):

 lista=list(map(int,input().split()))
 new_list=[]
 
 for i in range(len(lista)-1):
  
  new_list.append(lista[i]*lista[-1])
  
 if(sum(new_list)<=120):
  
  print('No')
  
 else:
  
  print('Yes')

