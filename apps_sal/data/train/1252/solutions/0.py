# cook your dish here
import math
N = 10**6
sum_arr = [0] * (N + 1) 
def lprime():
    arr = [0] * (N + 1) 
    arr[0] = 1
    arr[1] = 1
    for i in range(2, math.ceil(math.sqrt(N) + 1)): 
        if arr[i] == 0: 
            for j in range(i * i, N + 1, i): 
                arr[j] = 1
      
    curr_prime_sum = 0

    for i in range(1, N + 1): 
        if arr[i] == 0: 
            curr_prime_sum += i 
        sum_arr[i] = curr_prime_sum 
        
n=int(input())
lprime()
for _ in range(n):
    x=int(input())
    print(sum_arr[x]%10)
