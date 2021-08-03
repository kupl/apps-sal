from collections import Counter
class Solution:
    def wordSubsets(self, A, B):
        \"\"\"
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        \"\"\"
        wordsInBCounts = Counter()
        for wordB in B:
            counts = Counter(wordB)
            for (key,value) in counts.items():
                if wordsInBCounts[key] < value:
                    wordsInBCounts[key] = value        
        words = []        
        for wordA in A:
            stringALetterCounts = Counter(wordA)
            universal = True
            for (key,value) in wordsInBCounts.items():
                if value > stringALetterCounts[key]:
                    universal = False
                    break
            if universal:
                words.append(wordA)
        return words
