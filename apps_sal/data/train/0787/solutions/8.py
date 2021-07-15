for _ in range(int(input())):
 string = list(input())
 
 
 time = 0
 n = string.count('1')
 
 
 k = len(string)
 for _ in range(n):
  for i in range(k):
   if(string[i] == '1'):
    if(i == k-1):
     break
    j = i + 1
    while(string[j] != '1'):
     string[j-1] = '0'
     string[j] = '1'
     if(j-i == 1):
      time += 1
     time += 1
     if(j<k-1):
      j+= 1
     
   
   

    
  
 print(time)
