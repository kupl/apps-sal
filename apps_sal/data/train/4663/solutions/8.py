def order(sentence):
    data = sentence.split()

    result = []

    for word in data:
        for letter in word:
            if letter.isdigit():
                result.append([int(letter), word])

    return " ".join([x[1] for x in sorted(result)])
