def longest(s1, s2):
    # your code
    
    # Defining the Alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    # Concatenating the Two Given Strings
    s = s1 + s2
    
    # Declaring the Output Variable
    y = ""
    
    # Comparing whether a letter is in the string
    for x in alphabet:
      if x not in s:
        continue
      if x in s:
        y = y + x
        
    # returning the final output    
    return y
