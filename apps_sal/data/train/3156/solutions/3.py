def even_digit_squares(a, b):
    return [n**2 for n in range(int(a**0.5)+bool(a**0.5 % 1), int(b**0.5)+1) if not any(int(d) % 2 for d in str(n**2))]
    
    
    
    #result = []
    #i = int(a**0.5) + bool(a**0.5 % 1)
    #j = int(b**0.5) + 1
    #for n in range(i, j):
    #    sq = n**2
    #    if not any(int(d) % 2 for d in str(sq)):
    #        result.append(sq)
    #return result

