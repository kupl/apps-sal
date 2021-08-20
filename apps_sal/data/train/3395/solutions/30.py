def remove_duplicate_words(s):
    output = []
    s = s.split()
    for word in s:
        if word not in output:
            output.append(word)
    return ' '.join(output)
