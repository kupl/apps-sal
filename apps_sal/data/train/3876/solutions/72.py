def find(n):
    return sum([multiple for multiple in range(1,n+1) if multiple % 3 == 0 or multiple % 5 == 0])
