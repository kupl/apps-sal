class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        
        vowel_template = lambda w: w.lower().replace(\"a\", \"#\").replace(\"e\", \"#\").replace(\"i\", \"#\").replace(\"o\", \"#\").replace(\"u\", \"#\")
        
        exact_matches = set(wordlist)
        capital_matches = {w.lower() : w for w in wordlist[::-1]}
        vowel_matches = {vowel_template(w) : w for w in wordlist[::-1]}
        
        
        return [w if w in exact_matches else capital_matches.get(w.lower(), \"\") or vowel_matches.get(vowel_template(w), \"\") for w in queries]
