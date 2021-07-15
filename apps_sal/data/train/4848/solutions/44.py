def char_freq(message):    
    frequency_table = {}
    
    for char in message:
        frequency_table[char] = frequency_table.get(char, 0)+ 1

    return(frequency_table)

