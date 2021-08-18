def words_to_sentence(words):
    pass

    sentance = ""

    for word in words:
        sentance = (sentance + word + " ")

    return(sentance[0:(len(sentance) - 1)])
