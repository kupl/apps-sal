def to_freud(sentence):
    answer = []
    string = sentence.split()
    for word in string:
        x = word.replace(word, 'sex')
        answer.append(x)
    return ' '.join(answer)
