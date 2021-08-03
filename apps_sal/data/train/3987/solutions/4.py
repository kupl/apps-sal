def spin_words(sentence):
    words = sentence.split()
    output = []
    delimiter = " "
    for word in words:
        if len(word) >= 5:
            output.append(reverse(word))
        else:
            output.append(word)
    return delimiter.join(output)


def reverse(string):
    return string[::-1]
