class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:

        def wild_key(word):
            return \"\".join([\"*\" if c in vowels else c for c in word])
        
        vowels = {'a', 'e', 'i', 'o', 'u'}
        hs_word = set(); hs_lower = defaultdict(); hs_wild = defaultdict()
        for word in wordlist:
            hs_word.add(word)
            
            low_word = word.lower()
            if low_word not in hs_lower: hs_lower[low_word] = word
            
            wild_word = wild_key(low_word)
            if wild_word not in hs_wild: hs_wild[wild_word] = word
        
        res = []
        for query in queries:
            low_query  = query.lower()
            wild_query = wild_key(low_query)
            
            if   query      in hs_word : res.append(query)
            elif low_query  in hs_lower: res.append(hs_lower[low_query ])
            elif wild_query in hs_wild : res.append(hs_wild [wild_query])
            else                       : res.append(\"\")
        return res
\"\"\"
- problem
  * return word list, res[i]: correct word for query = queries[i]

- constraints & notes
  * n: len(wordlist)  , len(queries)   ; 1 <= n <= 5000
  * m: len(wordlist[i], len(queries[i]); 1 <= m <= 7
  * english letters

- solution
  * algorithm
    - 
    - 
    - precedence rules
      * query: exactly match -> return same word
      * query: matches w/ a workd up to capitalization, first such match in wordlist
      * query: matches w/ vowel error, return first match
      * no match: empty
    - helper
      * check capitalization
        - hash table: all wordlist
          hash table {\"k*t*\": [\"KiTe\", \"kite\" -> ordered with same order w/ wordlist]}
          query     : kite w/ k*t*
          * find if query in hash table
            - return first such match
      * check vowel error 
        * 
    
\"\"\"        
