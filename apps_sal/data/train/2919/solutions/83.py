def encode(message, key):
    L1="abcdefghijklmnopqrstuvwxyz";L2=[];number=0;L3=[]
    for i in message:
        L2.append(L1.index(i)+1+int(str(key)[number%len(str(key))]))
        number+=1
    return L2 
    
    

