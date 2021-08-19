def anagrams(word, words):

    def lettercount(inputword):
        wordarr = list(inputword)
        worddict = {}
        for letter in wordarr:
            if letter not in worddict:
                worddict[letter] = wordarr.count(letter)
        return worddict
    return [astring for astring in words if lettercount(astring) == lettercount(word)]
