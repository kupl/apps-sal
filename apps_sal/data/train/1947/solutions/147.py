def createHist(word):
    hist = {}
    for c in word:
        if c in list(hist.keys()):
            hist[c] += 1
        else:
            hist[c] = 1
    return hist


def isSubset(word1, word2Hist):
    word1Hist = createHist(word1)
    for c in list(word2Hist.keys()):
        if c in list(word1Hist.keys()):
            word1Occur = word1Hist[c]
            word2Occur = word2Hist[c]
            if word2Occur > word1Occur:
                return False
        else:
            return False
    return True


def isUniversal(word, bHist):
    if isSubset(word, bHist) == False:
        return False
    return True


def createMaxHistogram(arr):
    hist = {}
    for word in arr:
        wordHist = createHist(word)
        for key in list(wordHist.keys()):
            if key in list(hist.keys()):
                hist[key] = max(hist[key], wordHist[key])
            else:
                hist[key] = wordHist[key]
    return hist


class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        res = []
        bHist = createMaxHistogram(B)
        for word in A:
            if isUniversal(word, bHist):
                res.append(word)
        return res
