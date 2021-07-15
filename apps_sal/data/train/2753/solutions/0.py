def is_kiss(words):
    wordsL = words.split(' ')
    l = len(wordsL)
    for word in wordsL:
        if len(word) > l: return "Keep It Simple Stupid"
    return "Good work Joe!"
