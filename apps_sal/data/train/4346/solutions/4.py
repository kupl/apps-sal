def hidden(num):
    num_by_char = {
        '6': "a",
        '1': "b",
        '7': "d",
        '4': "e",
        '3': "i",
        '2': "l",
        '9': "m",
        '8': "n",
        '0': "o",
        '5': "t",
    }
    
    return ''.join(num_by_char[n] for n in str(num))

