def vowel_indices(word):
    retVal = [] # return list
    vow = ['a', 'e', 'i', 'o', 'u', 'y'] # vowel list
    word = word.lower() # make word all lowercase
    i = 1 # init position counter
    
    # loop through word and check for vowel
    for letter in word:
        # test for vowel
        if letter in vow:
            retVal.append(i) # append to return list
        i += 1 # inc position counter
    return retVal # return answer
