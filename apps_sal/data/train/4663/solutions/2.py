def order(sentence):
    if not sentence:
        return ''
    result = []
    split_up = sentence.split()
    for i in range(1, 10):
        for item in split_up:
            if str(i) in item:
                result.append(item)
    return ' '.join(result)
