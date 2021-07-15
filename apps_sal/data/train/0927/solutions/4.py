from collections import defaultdict 


def logic(temp, last, n, m):
  if m < 1:
   return 
  
  hash = defaultdict(bool) 
  for i in range(1, n + 1):
   hash[i] = True 
   
  temp -= last 
  first = 1 

  for i in range(m): 

   mohit_question = int(input() )
 
   if hash[mohit_question ]  : 
  
     temp += last 
     temp -= first 
     first, last = last, first #swap 
     print(temp + last)
     
     
   else:
     hash[last] = False 
     last = mohit_question 
     hash[last] = True 
     print(temp + last)
     
  
  
  
  
def main():       
  
  
  n, m = list(map(int, input(). split() ))
  
  
  
  
  temp = (n * (n + 1)) // 2 #total sum 
  
  last = n
  
  logic(temp,  last, n, m)
   

def __starting_point():
  main() 


__starting_point()
