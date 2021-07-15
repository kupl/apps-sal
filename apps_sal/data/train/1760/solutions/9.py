def count(chessBoard):
    c = chessBoard
    n = len(chessBoard)
    
    compteur = [0 for k in range(n+1)]
    copie = [[0 for k in range(n)] for j in range(n)]
    copie[0] = c[0]
    for k in range(1, n):
        copie[k][0] = c[k][0]
    
    for ligne in range(1, n):
        for col in range(1,n):
            if c[ligne][col]:
                valeur = 1+min(copie[ligne][col-1], copie[ligne-1][col-1], copie[ligne-1][col])
                copie[ligne][col] = valeur
                compteur[valeur] += 1
    
    for k in range(n-1, 1, -1):
        compteur[k] += compteur[k+1]
    
    d = {}          
    for k, v in enumerate(compteur):
        if v and k>1: d[k] = v
    return d

