def char_concat(word):
    return ''.join([(word[i]+word[-1-i]+str(i+1))for i in range(len(word)//2)])

