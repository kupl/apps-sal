def solve(s,g):
    try:
        return tuple(sorted([[x for x in list(range(1,s)) if x%g==0 and x+g==s][0], g])) 
    except IndexError:
        return -1
    
    
    
      


