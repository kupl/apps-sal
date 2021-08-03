class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        wordset = set(wordlist)
        wordset_lower = set()
        code_map = dict()
        for word in wordlist:
            wordset_lower.add(word.lower())
            code = encode(word)
            if code not in code_map:
                code_map[code] = word
        answer = []

        for query in queries:
            if query in wordset:
                answer.append(query)
            elif query.lower() in wordset_lower:
                for word in wordlist:
                    if word.lower() == query.lower():
                        answer.append(word)
                        break
            elif encode(query) in code_map:
                answer.append(code_map[encode(query)])
            else:
                answer.append('')

        return answer


def encode(word):
    code = []
    for c in word.lower():
        if c in {'a', 'e', 'i', 'o', 'u'}:
            code.append('@')
        else:
            code.append(c)
    return ''.join(code)
