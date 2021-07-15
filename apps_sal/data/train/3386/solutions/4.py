def get_column_title(num):
    if type(num) != int: raise TypeError
    if num < 1: raise IndexError
    
    abc = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    col_title = ""
    while num > 0:
        letter_index = num % 26
        if letter_index == 0:
            letter_index = 26
            num -= 26
        num //= 26
        col_title = abc[letter_index] + col_title
        
    return col_title.strip()

