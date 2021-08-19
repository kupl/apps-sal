def mutations(alice, bob, matchWord, first):
    winner = -1
    aliceWords = list(alice)
    bobWords = list(bob)
    aliceFoundAWord = bobFoundAWord = True
    matchingWordFound = True
    numOfIncorrectLetters = 0
    firstRound = -1
    i = 0
    if matchWord in aliceWords:
        del aliceWords[aliceWords.index(matchWord)]
    if matchWord in bobWords:
        del bobWords[bobWords.index(matchWord)]
    while aliceFoundAWord and bobFoundAWord and matchingWordFound or firstRound < 1:
        firstRound += 1
        i = 0
        numOfIncorrectLetters = 0
        matchingWordFound = False
        if not first:
            aliceFoundAWord = False
            for word in aliceWords:
                for letter in word:
                    if word.find(letter) != word.rfind(letter):
                        break
                    if letter != matchWord[i]:
                        numOfIncorrectLetters += 1
                    i += 1
                    if i == 4 and numOfIncorrectLetters == 1:
                        aliceFoundAWord = True
                        matchingWordFound = True
                        del aliceWords[aliceWords.index(word)]
                        matchWord = word
                        if matchWord in bobWords:
                            del bobWords[bobWords.index(word)]
                        break
                i = 0
                numOfIncorrectLetters = 0
                if aliceFoundAWord:
                    break
        else:
            bobFoundAWord = False
            for word in bobWords:
                for letter in word:
                    if word.find(letter) != word.rfind(letter):
                        break
                    if letter != matchWord[i]:
                        numOfIncorrectLetters += 1
                    i += 1
                    if i == 4 and numOfIncorrectLetters == 1:
                        bobFoundAWord = True
                        matchingWordFound = True
                        del bobWords[bobWords.index(word)]
                        matchWord = word
                        if matchWord in aliceWords:
                            del aliceWords[aliceWords.index(word)]
                        break
                i = 0
                numOfIncorrectLetters = 0
                if bobFoundAWord:
                    break
        first = not first
    if aliceFoundAWord:
        winner = 0
    elif bobFoundAWord:
        winner = 1
    else:
        winner = -1
    return winner
