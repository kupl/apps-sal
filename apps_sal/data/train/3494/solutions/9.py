def pig_it(text):
    piggy = []
    for word in text.split():
        if word.isalpha():
            piggy.append(word[1:] + word[0] + 'ay')
        else:
            piggy.append(word)
    return ' '.join(piggy)
