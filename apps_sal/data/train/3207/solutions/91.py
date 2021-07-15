def reverseWords(str):
    # Split the string on the spaces.
    list_words = str.split(" ")
    # Using the reversed() method to go over the list in a reversed order
    # Using the join() method to join the returning elements of the list.
    return ' '.join(reversed(list_words))
