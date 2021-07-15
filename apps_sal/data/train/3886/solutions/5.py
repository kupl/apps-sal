def is_prime(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if (n% 2 == 0 or n % 3 == 0):
        return False
    
    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
        
    return True

def total(arr):
    final = 0
    i = 0
    for num in arr:
        if is_prime(i) == True:
            final = final + arr[i]
            i = i + 1
        if i == len(arr):
            return final
        if not is_prime(i) == True:
            i = i + 1
        if i == len(arr):
            return final
    

            
    return final
    #lol i know it is too long; but I already did the 'Is a number prime?' Kata, and 
    #so I decided to use it here.

