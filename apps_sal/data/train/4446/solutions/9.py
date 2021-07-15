def words_to_sentence(words):
    sum = ""
    for i in range(len(words)):
        if i == len(words) - 1:
            sum = sum + words[i]
        else:
            sum = sum + words[i] + " "

    return sum
