def reverse(st):

    wordList = st.split(' ')[::-1]

    while("" in wordList):
        wordList.remove("")

    st = ' '.join(wordList)

    return st
