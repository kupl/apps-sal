def evil(n):
    count=0
    for x in str(bin(n)[2:]):
        if x=="1":
            count+=1
    return "It's Odious!" if count%2 else "It's Evil!"
        
    

