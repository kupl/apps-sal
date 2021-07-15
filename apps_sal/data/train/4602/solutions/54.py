# write the function is_anagram
def is_anagram(test, original):
    
    counter1=[0]*255
    counter2=[0]*255
    
    for i in range(len(test)):
        counter1[ord(test[i].lower())]+=1
    for i in range(len(original)):
        counter2[ord(original[i].lower())]+=1
        
    return (counter1==counter2)
    
    
    

