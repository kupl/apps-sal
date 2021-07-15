def reverse_words(text):
    split_text = text.split()
    sentence_list = []
    for word in split_text:
        reverseword_list = []
        for i in word:
            reverseword_list.append(i)
        sentence_list.append("".join(reverseword_list[::-1]))
    for i in range(len(text)-1):
        if text[i] == " " and text[i+1] == " ":
            return ("  ".join(sentence_list))
        if text[i] == " " and text[i+1] != " ":
            pass
    return (" ".join(sentence_list))


