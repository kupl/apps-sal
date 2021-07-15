def triple_trouble(one, two, three):
    new_string = ''
    for letter in range(len(one)):
        new_string += one[letter]
        new_string += two[letter] 
        new_string += three[letter]
    return new_string
