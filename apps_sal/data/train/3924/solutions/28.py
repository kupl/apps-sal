def reverse_words(text):

    new_text = ""

    for word in text.split(" "):

        new_text += (word[::-1] + " ")

    final = new_text[:-1]

    return final
