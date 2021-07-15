def evil(n):
    count = 0
    for x in bin(n):
        if x=='1':
            count+= 1
            
    return "It's Evil!" if count%2==0 else "It's Odious!"

