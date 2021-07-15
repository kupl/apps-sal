import re

def n00bify(text):
    replacementArray = [
    (r'too', "2"),
    (r'to', "2"),
    (r'fore', "4"),
    (r'for', "4"),
    (r'oo', "00"),
    (r'be', "b"),
    (r'are', "r"),
    (r'you', "u"),
    (r'please', "plz"),
    (r'people', "ppl"),
    (r'really', "rly"),
    (r'have', "haz"),
    (r'know', "no"),
    (r'\.', ""),
    (r',', ""),
    (r'\'', "")]
    
    firstLetterW = re.match(r'^w', text, flags=re.IGNORECASE)
    firstLetterH = re.match(r'^h', text, flags=re.IGNORECASE)
    
    for x in replacementArray:
        text = re.sub(x[0], x[1], text, flags=re.IGNORECASE)
        
    text = text.replace("s", "z")
    text = text.replace("S", "Z")
    
    count = 0
    for c in text:
        if (c.isalpha() or c.isdigit()) or c == " ":
            count += 1
        
    if firstLetterW  and count >= 28:
        text = "LOL OMG " + text
    elif firstLetterW :
        text = "LOL " + text
    elif count >= 32:
        text = "OMG " + text
        
    wordList = text.split()
    for i in range(len(wordList)):
        if i % 2 == 1 or firstLetterH:
            wordList[i] = wordList[i].upper()
    text = " ".join(wordList)
    
    text = text.replace("?", ("?" * len(wordList)))
    text = text.replace("!", exclamation(len(wordList)))
    
    return text
    
def exclamation(n):
    exclams = "!1" * (n // 2)
    if n % 2 == 1:
        exclams = exclams + "!"
    return exclams
