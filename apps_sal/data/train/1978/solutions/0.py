class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        out = []
        for word in words:
            pat_dict = dict()
            used = set()
            if len(word) == len(pattern):
                can_be = True
                for i in range(len(word)):
                    if word[i] not in pat_dict:
                        if pattern[i] not in used:
                            pat_dict[word[i]] = pattern[i]
                            used.add(pattern[i])
                        else:
                            can_be = False
                            break
                    else:
                        if pat_dict[word[i]] != pattern[i]:
                            can_be = False
                            break
                if can_be == True:
                    out.append(word)
        return out
