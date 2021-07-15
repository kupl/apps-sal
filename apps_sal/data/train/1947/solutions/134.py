class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        
        ans = []
        wordCountA = [ self.genWordCount(word) for word in A]
        wordCountB = [ self.genWordCount(word) for word in B]
        reducedWordB = {}
        for wordDict in wordCountB:
            for key, val in wordDict.items():
                reducedWordB[key] = max(reducedWordB[key], val) if key in reducedWordB else val

        for i in range(len(A)):
            if self.isSubset(wordCountA[i], reducedWordB):
                ans.append(A[i])

        return ans
    
    def genWordCount(self, word):
        wordCount = {}
        for c in word:
            if c in wordCount:
                wordCount[c] += 1
            else:
                wordCount[c] = 1
        return wordCount
    
    def isSubset(self, dictA, dictB):
        for key, val in dictB.items():
            if key not in dictA or dictA[key] < val:
                return False
        return True
