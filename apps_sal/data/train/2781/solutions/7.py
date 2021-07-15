def longest_collatz(input_array):
    results = {1: 1}
    
    for n in range(2, max(input_array) + 1):
        count = 0
        x = n
        while x not in results:
            x = x * 3 + 1 if x % 2 else x // 2
            count += 1
        
        count += results[x]
        results[n] = count
    
    return max(input_array, key=results.get)
