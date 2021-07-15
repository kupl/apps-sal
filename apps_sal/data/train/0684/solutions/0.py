# cook your dish here
import math   
  
# Function to find the Largest  
# Odd Divisor Game to check 
# which player wins  
def findWinner(n, k):  
      
    cnt = 0;  
  
    # Check if n == 1 then  
    # player 2 will win  
    if (n == 1): 
        print("Grinch");  
  
    # Check if n == 2 or n is odd  
    elif ((n & 1) or n == 2): 
        print("Me");  
  
    else: 
        tmp = n;  
        val = 1;  
  
        # While n is greater than k and  
        # divisible by 2 keep  
        # incrementing tha val  
        while (tmp > k and tmp % 2 == 0):  
            tmp //= 2;  
            val *= 2;  
              
        # Loop to find greatest  
        # odd divisor  
        for i in range(3, int(math.sqrt(tmp)) + 1):  
            while (tmp % i == 0): 
                cnt += 1;  
                tmp //= i;  
          
        if (tmp > 1): 
            cnt += 1;  
  
        # Check if n is a power of 2  
        if (val == n): 
            print("Grinch");  
  
        elif (n / tmp == 2 and cnt == 1): 
            print("Grinch");  
  
        # Check if cnt is not one  
        # then player 1 wins  
        else: 
            print("Me");  
              
# Driver code  
def __starting_point():  
    for i in range(int(input())):
        n=int(input()) 
        findWinner(n, 1);  
__starting_point()
