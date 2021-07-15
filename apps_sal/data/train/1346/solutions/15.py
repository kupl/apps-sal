# Python3 program to find total possible 
# numbers with n digits and weight w 

# Function to find total possible 
# numbers with n digits and weight w 
def findNumbers(n, w): 

 x = 0; 
 s = 0; 

 # When Weight of an integer 
 # is Positive 
 if (w >= 0 and w <= 8): 
  # Subtract the weight from 9 
  x = 9 - w; 
 
 # When weight of an integer 
 # is negative 
 elif (w >= -9 and w <= -1): 
  
  # add the weight to 10 to 
  # make it positive 
  x = 10 + w; 
 
 s = pow(10, n - 2); 
 s = (x * s); 
 
 return s; 

# Driver code 

# number of digits in an 
# integer and w as weight 


# This code is contributed 
# by mits
m = 10**9 + 7
for _ in range(int(input())):
 n,w = list(map(int,input().split()))
 print(findNumbers(n,w)%m)

