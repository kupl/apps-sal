def reverse(st):
    
    # split the string into different words
    wordList = st.split(' ')[::-1]
        
    # remove spaces
    while("" in wordList):
        wordList.remove("")
       
    st = ' '.join(wordList)
    
    return st
