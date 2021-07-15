def knight_rescue(N,x,y):
    return (y - x) % 2 == 0 or any(n % 2 == 0 for n in N)

