def hotpo(n):
    counter = 0
    while n != 1:
        n = 3 * n + 1 if n % 2 else n/2
        counter += 1
    return counter
            
    
'''
if(number is even) number = number / 2
if(number is odd) number = 3*number + 1
make a function hotpo that takes a positive n as input
and returns the number of times you need to perform this algorithm to get n = 1.

'''
