def match(query, wordsSet):
    if query in wordsSet:
        return True, query
    return False, \"\"

def capitalization(query, lowerWordsSet):
    if query.lower() in lowerWordsSet:
        return True, lowerWordsSet[query.lower()]
    return False, \"\"

def vowelErrors(query, lowerAndWithoutVowelsSet):
    vowelsRemoved = query.lower().replace('a', '*').replace('e', '*').replace('i', '*').replace('o', '*').replace('u', '*')
    if vowelsRemoved in lowerAndWithoutVowelsSet:
        return True, lowerAndWithoutVowelsSet[vowelsRemoved]
    return False,  \"\"          


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        answer = []
        wordsSet = set(wordlist)
        lowerWordsList = {}
        lowerAndWithoutVowelsSet = {}
        for word in wordlist:
            lowerWordsList.setdefault(word.lower(), word)
            vowelsRemoved = word.lower().replace('a', '*').replace('e', '*').replace('i', '*').replace('o', '*').replace('u', '*')
            lowerAndWithoutVowelsSet.setdefault(vowelsRemoved, word)
        
        for i, query in enumerate(queries):
            res, toAdd = match(query, wordsSet)
            if res:
                answer.append(toAdd)
            else:
                res, toAdd = capitalization(query, lowerWordsList)
                if res:
                    answer.append(toAdd)
                else:
                    res, toAdd = vowelErrors(query, lowerAndWithoutVowelsSet)
                    if res:
                        answer.append(toAdd)
                    else:
                        answer.append(\"\")
        return answer
