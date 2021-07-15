def count_sheep(n):
    x = 0
    s=[]
    while x < n: 
        for _ in range(n):
            x+=1
            s.append (f"{x} sheep...")
    return "".join(s) 

