def reverse_letter(string):
    result=""
    for letter in string:
        if letter.isalpha():
           result+=letter
        else:
           del(letter)
    result2=result[::-1]
    return(result2)

