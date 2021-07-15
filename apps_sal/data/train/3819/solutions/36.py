def smash(words):
    
    ##set up empty string
    x = ""
    
    ##loop over words in the array, adding each word to the empty string x, followed by a space
    for i in range(len(words)):
        x = x+words[i]+" "
        
    ##lazy coding: remove extra space from end of final string

    x = x[:-1]
    print(x)
    return(x)
    #print(x+words[L-1])

