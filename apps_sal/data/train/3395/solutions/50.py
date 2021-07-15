def remove_duplicate_words(s):
    output = []
    for word in s.split():
        if not word in output: output.append(word)
    return ' '.join(output)
