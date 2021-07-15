#import string so we can generate the alphabets using string.ascii
import string

def alphabet_position(text):
    lower_case_text = text.lower() #convert the given text into all lowercase letters
    alphabet = string.ascii_lowercase # generate lowercase letters from the string module
    number = list(range(1, 27)) #generate numbers from 1-26
    dict_alphabet_number = dict(list(zip(alphabet, number))) # combine the aphabets in a dictionary using dict and zip
    collector = [] # create a container to old the numbers generated from the loop
    
    for element in lower_case_text: 
        if element in alphabet:
            collector.append(str(dict_alphabet_number[element])) 
    return ' '.join(collector)
    
            
            

