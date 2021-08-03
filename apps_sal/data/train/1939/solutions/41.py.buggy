class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        res = []
        # if totally same, then put that exact one
        # if case-insensitively same, then earlier one
        # check if indices for vowels are same, if same, then true
        
        vowels = [\"a\", \"e\", \"i\", \"o\", \"u\"]
        
        lookup = {}
        for word in wordlist:
            if not lookup.get(word.lower(), None):
                lookup[word.lower()] = word
                lookup[word] = word
                preprocessed_word = \"\".join([\"#\" if letter.lower() in vowels else letter.lower() for letter in word])
                if not lookup.get(preprocessed_word, None):
                    lookup[preprocessed_word] = word
            else:
                if not lookup.get(word, None):
                    lookup[word] = word
        
        
        for query in queries:
            # if totally same, then put that exact one
            # the_word = lookup.get(query, None)
            if query in lookup.keys() and query in wordlist:
                res.append(query)
                continue
                
            # if case-insensitively same, then earlier one
            the_word = lookup.get(query.lower(), None)
            if the_word:
                res.append(the_word)
                continue
            
            # check if indices for vowels are same, if same, then true
            preprocessed_query = \"\".join([\"#\" if letter.lower() in vowels else letter.lower() for letter in query])
            the_word = lookup.get(preprocessed_query, None)
            if the_word:
                res.append(the_word)
                continue
            
            res.append(\"\")
        
        return res
            
