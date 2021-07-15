# cook your dish here
import math
def find(n):
    cnt=0
    if n==0:
        return 1
    if (n == 1): 
        return 0
    elif ((n & 1) or n == 2): 
        return 1
  
    else: 
        tmp = n;  
        val = 1;  
        k=1
        while (tmp > k and tmp % 2 == 0):  
            tmp //= 2;  
            val *= 2
        for i in range(3, int(math.sqrt(tmp)) + 1):  
            while (tmp % i == 0): 
                cnt += 1;  
                tmp //= i;  
        if (tmp > 1): 
            cnt += 1;  
        if (val == n): 
            return 0 
  
        elif (n // tmp == 2 and cnt == 1): 
            return 0 
        else: 
            return 1
t=int(input())
for i in range(t):
    n=int(input())
    if find(n):
        print("Me")
    else:
        print("Grinch")
