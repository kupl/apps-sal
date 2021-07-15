def encode(message, key):
    
    indexKey = 0 
    l = [ord(m)- 96 for m in message]

    for i in range(len(message)):       
        l[i] +=  int ( str(key)[indexKey] )
        indexKey =  ( indexKey + 1) % len(str(key))
        
    return l
        

