def reverse_words(text):
  # Splitting the Sentence into list of words.
    words = text.split(" ")

    # Reversing each word and creating
    # a new list of words
    # List Comprehension Technique
    newWords = [word[::-1] for word in words]

    # Joining the new list of words
    # to for a new Sentence
    print(newWords)
    newSentence = " ".join(newWords)

    return newSentence
