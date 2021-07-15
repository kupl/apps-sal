def letter_to_int(letter):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    return alphabet.index(letter) + 1
def solve(arr):
    result = []
    arr = [i.lower() for i in arr]
    for word in arr:
        counter = 0
        for i in range (0,len(word)):
            if letter_to_int(word[i]) == i+1:
                counter = counter+1
        result.append(counter)        
    return(result)    
