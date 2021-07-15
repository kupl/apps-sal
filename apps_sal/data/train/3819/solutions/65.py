def smash(words):
    # Begin here
    count = 0
    sentence = ""
    for word in words:
        sentence += word
        if count != len(words) - 1:
            sentence += " "
        count += 1
    return sentence

