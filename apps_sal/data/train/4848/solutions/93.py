def char_freq(message):
    arr=list(message)  
    arr=list(dict.fromkeys(arr))
    res={}
    for i in arr:
        res[i]=message.count(i) 
    return res
