def reverse_words(text):
    tempWord = ""
    result = ""
    for i in range(len(text)):
        if text[i] != " ":
            tempWord += text[i]
            if i == len(text) - 1:
                result += tempWord[::-1]
        else:
            if text[i - 1] != " ":
                result += tempWord[::-1] + " "
                tempWord = ""
            else:
                result += " "
    return result
