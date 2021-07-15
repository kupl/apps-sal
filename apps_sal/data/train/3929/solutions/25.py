def reverse(st):
    #Split creates a list with all the words in it, separated
    words = st.split()
    #Joins them back together to a string
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence
