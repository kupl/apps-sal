def encode(message, key):
    key_list = list(str(key))
    encoded_list = []
    k = 0
    for letter in message:
        
        letter_digit = ord(letter) - 96
        
        letter_digit_encoded = letter_digit + int(key_list[k%len(key_list)])
        
        encoded_list.append(letter_digit_encoded)
        
        k += 1
        
    return encoded_list
        

