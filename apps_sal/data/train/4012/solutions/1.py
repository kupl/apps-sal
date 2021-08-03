import numpy as np


def encrypt(text, key):
    # Declare string variable to store the answer
    ans = ''
    # Covert all the alphabets to upper case and clean everything else
    clean_text = ''.join([i.upper() for i in text if i.isalpha()])
    # Add Z to the cleaned text if the length of it is odd
    clean_text += 'Z' * (len(clean_text) % 2)
    # Return empty string if the cleaned text is empty
    if len(clean_text) == 0:
        return ''
    # Find the key matrix
    km = np.matrix([[ord(key[0]) - 97, ord(key[1]) - 97], [ord(key[2]) - 97, ord(key[3]) - 97]])
    # Create a text matrix
    tm = np.matrix([[ord(clean_text[i]) - 65, ord(clean_text[i + 1]) - 65] for i in range(0, len(clean_text), 2)]).T
    # Multiply the key matrix by the text matrix and apply modulo 26
    am = (km * tm) % 26
    # Convert the numbers back to letters and append them to the ans variable
    for i in np.array(am.T):
        ans += chr(i[0] + 65)
        ans += chr(i[1] + 65)
    # Return the answer variable
    return ans
