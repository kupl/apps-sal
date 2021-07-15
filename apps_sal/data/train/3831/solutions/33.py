
# Python3 implementation of the approach 
  
# Function to return the sum of internal  
# angles of an n-sided polygon 
def angle(n): 
    if(n < 3): 
        return 0
    return ((n - 2) * 180) 
  
# Driver code 
n = 5
print((angle(n))) 

