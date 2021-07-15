def find(n):
    resultat = sum([i for i in range(n+1) if i%3==0 or i%5==0])
    return resultat


