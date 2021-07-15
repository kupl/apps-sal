def reverse_words(text):
    text_split = text.split(" ")
    index = 0
    for t in text_split:
        text_split[index] = "".join(reversed(t))
        index += 1
    
    return (" ".join(text_split))
