def reverser(sentence):
    ans = ''
    word = ''
    for letter in sentence:
        if letter == ' ':
            ans = ans + word[::-1] + letter
            word = ''
        else:
            word = word + letter
    return ans + word[::-1]
