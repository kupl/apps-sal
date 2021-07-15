words = "zero one two three four five six seven eight nine".split()
wordify = lambda n: "".join(words[int(d)] for d in str(n))


def numbers_of_letters(n):
    result = [wordify(n)]
    while result[-1] != "four":
        result.append(wordify(len(result[-1])))
    return result
