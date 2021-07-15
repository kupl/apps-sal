def encrypt(text):

    import string

    #prechecks

    char_filter = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,:;-?! '()$%&" + '"'
    char_filter = [char for char in char_filter]
    
    if text == "" or text is None:
        return text
    else:
        for char in text:
            if char not in char_filter:
                raise Exception("text contains invalid character")

        #turn text to list
        txt_list = [char for char in text]

        #step 1
        for charIndex in range(1, len(txt_list), 2):

            if txt_list[charIndex] in string.ascii_uppercase:
                txt_list[charIndex] = txt_list[charIndex].lower()

            elif txt_list[charIndex] in string.ascii_lowercase:
                txt_list[charIndex] = txt_list[charIndex].upper()

        #step 2
        for i in range(len(txt_list)-1):
            #x = len-i makes it go through list in reverse order
            x = len(txt_list) - 1 - i
            char2 = char_filter.index(txt_list[x])
            char1 = char_filter.index(txt_list[x - 1])
            txt_list[x] = char_filter[char1-char2]

        #step 3
        char = char_filter.index(txt_list[0])
        txt_list[0] = char_filter[char * - 1 - 1]

        #convert list to text
        text = ""
        for char in txt_list:
            text += char

        return text
    

def decrypt(text):

    import string

    #prechecks

    char_filter = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,:;-?! '()$%&" + '"'
    char_filter = [char for char in char_filter]
    if text == "" or text is None:
        return text
    else:
        for char in text:
            if char not in char_filter:
                raise Exception("text contains invalid character")
    
        #turn text to list
        txt_list = [char for char in text]

        #step 3 reverse
        txt_list[0] = char_filter[77 - char_filter.index(txt_list[0]) - 1]

        #step 2 reverse
        for i in range(1, len(txt_list)):
            txt_list[i] = char_filter[char_filter.index(txt_list[i - 1]) - char_filter.index(txt_list[i])]

        #step 1 reverse

        for charIndex in range(1, len(txt_list), 2):

            if txt_list[charIndex] in string.ascii_uppercase:
                txt_list[charIndex] = txt_list[charIndex].lower()

            elif txt_list[charIndex] in string.ascii_lowercase:
                txt_list[charIndex] = txt_list[charIndex].upper()

        #convert list to text
        text = ""
        for char in txt_list:
            text += char

        return text
