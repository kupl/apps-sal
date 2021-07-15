from collections import defaultdict

def three_amigos(numbers):
    amigos = defaultdict(list)
    
    for i in range(len(numbers)-3 +1):
        a, b, c = numbers[i:i+3]
        
        if a%2 == b%2 == c%2:
            rnge = max(a, b, c) - min(a, b, c)
            amigos[rnge].append([a, b, c])
    
    return amigos[min(amigos.keys())][0] if amigos else []
