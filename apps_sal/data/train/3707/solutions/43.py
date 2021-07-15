import re
def sorter(textbooks):
    textbooks.sort(key=str.lower) 
    return textbooks
    #Cramming before a test can't be that bad?
    #print(re.findall(r"\S",textbooks,re.IGNORECASE))
    #return sorted(textbooks)

