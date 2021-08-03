class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def insert(word, trie):
            node = trie
            for letter in word:
                if letter in 'aeouiAEOUI':
                    key = '*'
                else:
                    key = letter.lower()
                if not key in node:
                    node[key] = {}
                node = node[key]
            if not '$' in node:
                node['$'] = OrderedDict()
            node['$'][word] = True

        def find(word, trie):
            node = trie
            matched = ''
            for letter in word:
                if letter in 'aeouiAEOUI':
                    key = '*'
                else:
                    key = letter.lower()
                if not key in node:
                    return matched
                node = node[key]
            if '$' in node:
                if word in node['$']:
                    return word
                else:
                    k = 0
                    for word_i in node['$'].keys():
                        if k == 0:
                            matched = word_i
                        if word.lower() == word_i.lower():
                            return word_i
                        k += 1
                    return matched
            else:
                return matched

        trie = {}
        for i, word in enumerate(wordlist):
            insert(word, trie)
        ans = []
        for q in queries:
            ans.append(find(q, trie))

        return ans
