def solution(string):
    #Empty string for holding reversed string
    reverse = ""
    letter_index = len(string)-1
    #Loop through for each letter
    for x in range(len(string)):
        #The reverse string gets the end letter added to it and then the next earlier one
        reverse = reverse + string[letter_index]
        #Move to next letter
        letter_index-=1
    return reverse
