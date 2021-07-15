from operator import itemgetter

class Solution:
    def arrangeWords(self, text: str) -> str:
        words = [[str.lower(v), k, len(v)] for k,v in enumerate(text.split(' '))]
        words2 = sorted(words, key=itemgetter(2))
        print(words)
        print(words2)
        words3 = [word[0] for word in words2]
        print(words3)
        
        words4 = [str.title(words3[x]) if x == 0 else words3[x] for x in range(len(words3))]
        return ' '.join(words4)
