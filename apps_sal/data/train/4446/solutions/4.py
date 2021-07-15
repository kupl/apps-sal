def words_to_sentence(words):
    sentence = ""
    for i in range(len(words)):
        if i == len(words) - 1:
            sentence += words[i]
        else:
            sentence += words[i] + " "
        
    return sentence
