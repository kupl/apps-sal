def remove_duplicate_words(s):
    array = s.split()
    output = []
    for word in array:
        if word not in output:
            output.append(word)
    return ' '.join(output)
