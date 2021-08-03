class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        
        m_cap = {}
        for word in wordlist:
            new_ = []
            for c in word:
                new_.append(c.lower())
            new_ = ''.join(new_)
            if new_ not in m_cap:
                m_cap[new_] = word
        # print(m_cap)
        
        m_devow = {}
        for word in wordlist:
            new_ = []
            for c in word:
                c = c.lower()
                if c in set(['a','e','i','o','u']):
                    c = '*'
                new_.append(c.lower())
            new_ = ''.join(new_)
            if new_ not in m_devow:
                m_devow[new_] = word
        # print(m_devow)
        
        wordlist = set(wordlist)
        
        res = []
        for query in queries:
            if query in wordlist:
                res.append(query)
                continue
            
            lower_case = []
            for c in query:
                lower_case.append(c.lower())
            lower_case = ''.join(lower_case)
            if lower_case in m_cap:
                res.append(m_cap[lower_case])
                continue
            
            devowel = []
            for c in query:
                c = c.lower()
                if c in set(['a','e','i','o','u']):
                    c = '*'
                devowel.append(c)
            devowel = ''.join(devowel)
            if devowel in m_devow:
                res.append(m_devow[devowel])
                continue
            
            res.append(\"\")
        return res
        
                    
