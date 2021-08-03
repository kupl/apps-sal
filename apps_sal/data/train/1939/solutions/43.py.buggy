class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        wordSet = set(wordlist)
        res = []
        words_dict = collections.defaultdict(list)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for i in range(len(wordlist)):
            word = wordlist[i]
            words_dict[word.lower()].append(i)
            wild_word = word.lower()
            for vowel in vowels:
                wild_word = wild_word.replace(vowel, '*')
            words_dict[wild_word.lower()].append(i)
        print(words_dict)
        for query in queries:
            wild_query = query.lower()
            for vowel in vowels:
                wild_query = wild_query.replace(vowel, '*')                    
            if query in wordSet:
                res.append(query)
            elif query.lower() in words_dict:
                res.append(wordlist[words_dict[query.lower()][0]])
            elif wild_query.lower() in words_dict:
                res.append(wordlist[words_dict[wild_query.lower()][0]])
            else:
                res.append(\"\")
        return res
