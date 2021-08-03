def vowel_indices(word):
    retVal = []
    checkList = "aeiouy"
    for i, x in enumerate(word.lower()):
        print(("Looking at ", x))
        try:
            l = checkList.index(x)
            retVal.append(i + 1)
            print(("think this is a vowel", x))
        except ValueError:
            print(("discarded", x))
    return retVal


#    word= list(word)
#    retVal=[]
#    for x in word:
#        x=x.lower()
#        if x=="a" or x=="e" or x=="i" or x=="o" or x=="u" or x=="y":
#            print("think this is a vowel",x)
#            retVal.append(word.index(x)+1)
#            print(x)
#        else:
#            print("discarded",x)
#    return retVal
