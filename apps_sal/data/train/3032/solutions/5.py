from collections import Counter

def factors(n):
    result = set()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            result.add(i)
            result.add(n // i)
    return sorted(result) if result else ['None']
    
def factorsRange(n, m):
    return {i: factors(i) for i in range(n, m+1)}
