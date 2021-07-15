def automorphic(n):
    
    sq = n * n
    
    if str(sq).endswith(str(n)):
        return "Automorphic"
        
    else:
        return "Not!!"
