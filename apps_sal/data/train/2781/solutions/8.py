def collatz(n):
    d = {1:1}
    count = 0
    while n != 1:    
        if n in d:
            count += d[n]
            n = 1
        else:
            if n % 2 == 0:
                n /= 2
                count += 1
            else:
                n = (3*n + 1)/2
                count += 2      
    return count 

def longest_collatz(input_array):
    return max(input_array, key=collatz)
