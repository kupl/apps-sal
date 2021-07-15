for _ in range(int(input())):
 s = input()
 
 
 d = {'0':0, '1':0}
 for i in s:
   d[i] += 1 
 
 if(len(s)%2 or d['1']==0 or d['0'] == 0):
  print(-1)
 else:
  print(abs(d['1'] - d['0']) //2)
   
 

