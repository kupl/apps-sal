def reverse_words(text):
    text = text.replace(" ", "\n<SP>\n").lstrip("\n").split("\n") 
    output = []
    for word in text:
        if word != "<SP>":output.append(word[::-1])
        else:output.append(word)
    return str("".join(output)).replace("<SP>"," ")

