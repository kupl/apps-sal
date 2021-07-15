def contamination(text,char):
    if text == "":
        return text
    elif char == "":
        return char
    else:
        count_of_characters = len(text)
        return (char * count_of_characters)

