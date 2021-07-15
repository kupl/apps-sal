import math
def CountFrequency(my_list): 
 
 # Creating an empty dictionary  
 freq = {} 
 x=[]
 for item in my_list: 
  if (item in freq): 
   freq[item] += 1
  else: 
   freq[item] = 1
 
 for key, value in freq.items():
  x.append(math.ceil(value/2))
 return(sum(x))
   
n=int(input())
a=list(map(int, input().split()))[:n]
print(CountFrequency(a))
