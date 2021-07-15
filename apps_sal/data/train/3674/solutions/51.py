def add_binary(a,b):
    #create a string variable with the sum of the given numbers, and convert that sum to binary
    string = bin(a + b)
    #Take out the first 2 characters of the "binary" strings and return  
    return string.replace('0b', '')  
