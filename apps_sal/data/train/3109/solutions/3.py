import string


def scramble_words(words):
    if (len(words) <= 1):
        return words

    words = words.split(" ")

    pureWords = []

    sChars = []

    for i in range(len(words)):
        flag = 0
        for l in words[i][1:]:
            if l != words[i][0]:
                flag = 1
        if flag == 0:
            words[i] = words[i][0]
        pureWords.append('')
        for j in range(len(words[i])):
            if words[i][j] in string.ascii_letters:
                pureWords[i] += words[i][j]
            else:
                sChars.append((j, words[i][j]))

        if (len(words[i]) == 1):
            pureWords[i] = words[i]
        else:
            pureWords[i] = pureWords[i][0] + ''.join(sorted(pureWords[i][1:-1])) + pureWords[i][-1]
            currWord = [l for l in pureWords[i]]
            for index, char in sChars:
                currWord.insert(index, char)
            pureWords[i] = ''.join(currWord)

        sChars = []

    return ' '.join(pureWords)
