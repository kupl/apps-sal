# cook your dish here
def PrintBothArrays(a, n) : 
 
 # Store both arrays  
 v1, v2 = [], [] 
 
 # Used for hashing  
 mpp = dict.fromkeys(a, 0) 
 
 # Iterate for every element  
 for i in range(n) : 
 
  # Increase the count  
  mpp[a[i]] += 1 
 
  # If first occurrence  
  if (mpp[a[i]] == 1) : 
   v1.append(a[i]) 
 
  # If second occurrence  
  elif (mpp[a[i]] == 2) :  
   v2.append(a[i]) 
 
  # If occurs more than 2 times  
  else :  
   print("NO") 
   return;  
 
 # Sort in increasing order
 maximum=max(v1)
 if maximum in v2:
  print("NO")
  return;
 
 v1.sort();  
 
 # Print the increasing array  
 print("YES");  
 for it in v1: 
  print(it, end = " ");  
 
 # Sort in reverse order  
 v2.sort(reverse = True);  
 
 # Print the decreasing array 
 for it in v2 :  
  print(it, end = " ") 
 print()
 
# Driver code  
def __starting_point(): 
 try:
  t=int(input())
  for _ in range(t):
   n=int(input())
   a=list(map(int,input().split())) 
   PrintBothArrays(a, n); 
 except EOFError as t : pass
__starting_point()
