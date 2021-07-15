def pig_it(text):
    #your code here
    n = 0
    x = 0
    text = text.split() #split the text into words
    text = list(text) #make the words a list
    pig_text = [] #make an empty list
    for word in text:
        a = list(word) #set a to be the list of word (the letters on their own)
        print(a)
        if len(a) > 1:
            a.append(a[0]) #add the first letter to the end
            del a[0] #delete the first letter
            a.append('ay') #add ay to the end
        if '!' in a:
            n += 1
        elif '?' in a:
            x += 1
        elif len(a) == 1:
            print(a)
            a.append('ay') 
        a = ''.join(a) #rejoin the word
        pig_text.append(a) #put the word in the empty list
    pig_text = ' '.join(pig_text) #join the words up with spaces
    return pig_text #return the sentence
