class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = {}
        for word in words:
            curnode = self.root
            for ch in word:
                if ch not in curnode:
                    curnode[ch] = {}
                curnode = curnode[ch]
            curnode['is_end'] = True
        self.leads = [self.root]

    def query(self, letter: str) -> bool:
        next_leads = [self.root]
        found_word = False
        for lead in self.leads:
            if letter in lead:
                new_lead = lead[letter]
                next_leads.append(new_lead)
                if 'is_end' in new_lead:
                    found_word = True
        self.leads = next_leads
        return found_word
