def is_haiku(text):
    temp=text.replace(".","").replace(",","").replace("-","").replace("?","").replace("!","").replace("#","").replace(";","").replace("/","").replace(":","").replace(")","").replace("()","")
    temp=temp.lower()
    temp=temp.split("\n")
    haiku=[]
    count=0
    for i in temp:
        for word in i.split():
            count+=syllable(word)
        haiku.append(count)
        count=0
    if len(haiku)!=3:
        return False   
    return True if (haiku[0]==5 and haiku[1]==7 and haiku[2]==5) else False
def syllable(text):
    count=0
    index=0
    while index<len(text):
        if text[index] in "aeiouy":
            if text[index]=="e" and index==len(text)-1:
                break
            count+=1
            while (index+1)<len(text):                
                if not (text[index+1] in "aeiouy"):
                    break
                index+=1
        index+=1
    if count==0:
        count=1
    return count
