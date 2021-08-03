class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        exact = {word: word for word in wordlist}
        caps = {word.lower(): word for word in wordlist[::-1]}
        vowel = defaultdict(lambda: '')
        
        _vowels = set('aeiou')
        for word in wordlist[::-1]:
            orig_word, word = word, word.lower()\\
                                        .replace('a', '$')\\
                                        .replace('e', '$')\\
                                        .replace('i', '$')\\
                                        .replace('o', '$')\\
                                        .replace('u', '$')
            vowel[word] = orig_word
                
        ans = deque()
        for query in queries:
            if query in exact:
                ans.append(exact[query])
            elif query.lower() in caps:
                ans.append(caps[query.lower()])
            else:
                query = query.lower().replace('a', '$')\\
                                    .replace('e', '$')\\
                                    .replace('i', '$')\\
                                    .replace('o', '$')\\
                                    .replace('u', '$')
                
                ans.append(vowel[query])
        return ans
