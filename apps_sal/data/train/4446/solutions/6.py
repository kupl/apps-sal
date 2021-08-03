def words_to_sentence(words):
    pass

# =============================================================================
#     This function creates a sentance string from a list of word strings,
#     separated by space.
#
#     Example:
#         ["hello", "world"] -> "hello world"
# =============================================================================

    sentance = ""

    for word in words:
        sentance = (sentance + word + " ")

    return(sentance[0:(len(sentance) - 1)])
