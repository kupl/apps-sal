def remove_duplicate_words(s):
    list_of_words = s.split()
    compressed = []
    for word in list_of_words:
        if word not in compressed:
            compressed.append(word)
        else:
            pass
    compressed_to_string = ' '.join(compressed)
    return compressed_to_string
