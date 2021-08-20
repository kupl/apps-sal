def high(x):
    highest_score = 0
    for word in x.split(' '):
        score = sum((ord(c) - 96 for c in word))
        if score > highest_score:
            highest_score = score
            highest_word = word
    return highest_word
