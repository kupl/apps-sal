def T9(words,seq):
    result = []
    seq = list(seq)
    numToword(int(seq[0]))
    for word in words:
        if (isWord(word,seq)):
            result.append(word)
    if(len(result)):
        return result
    red = ""
    for i in seq:
        red += numToword(int(i)-1)[0]
    result.append(red.lower())
    return result
        
def numToword(num):
    return ([" ","ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ",""])[num]
# Return true if we can write this word with this leters
def isWord(word,num):
    if(len(word) != len(num)):
        return False
    for i_n in range(len(word)):
        if (word[i_n].upper() in numToword(int(num[i_n])-1))==False:
            return False
    return True
