def reverse_words(text):
    arr=text.split(" ")
    resarr=[]
    t=" "
    for i in arr:
        a=[]
        s=""
        for j in i:            
            a.insert(0,j)
        resarr.append(s.join(a))
    return t.join(resarr)   
        
  #go for it

