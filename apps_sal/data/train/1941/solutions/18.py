class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        res = []
        cnt = collections.Counter(''.join(sorted(set(w))) for w in words)
        for p in puzzles:
            bfs = [p[0]]
            for c in p[1:]:
                bfs += [s + c for s in bfs]
            res.append(sum(cnt[''.join(sorted(s))] for s in bfs))
        return res

#         wordCounter = defaultdict(int)
#         chars = \"abcdefghijklmnopqrstuvwxyz\"
#         shiftDict = {chars[i]: (1<<(ord(chars[i]) - 97)) for i in range(26)}
#         wordCounter1 = Counter(\"\".join(sorted(set(word))) for word in words)

#         for word in wordCounter1:
#             mask = 0
#             for char in word:
#                 mask |= shiftDict[char]
#             wordCounter[mask] += wordCounter1[word]

#         ans = []
#         maxMask = (1<<26)-1
#         dp = {}
#         for puzzle in puzzles:
#             pMask = 0
#             for char in set(puzzle):
#                 pMask |= shiftDict[char]
#             pMask ^= maxMask
#             subAns = 0
#             if (pMask, puzzle[0]) in dp:
#                 ans.append(dp[(pMask, puzzle[0])])
#             else:
#                 for wMask in wordCounter:
#                     if wMask & shiftDict[char] and (wMask & pMask == 0):
#                         subAns += wordCounter[wMask]
#                 dp[(pMask, puzzle[0])] = subAns
#                 ans.append(subAns)
#         return ans

        # charSetDict = defaultdict(set)
        # wordSubSetDict = {}
        # for word in words:
        #     wordSubSetDict[word] = set(word)
        #     for char in word:
        #         charSetDict[char].add(word)
        # ans = []
        # for puzzle in puzzles:
        #     subAns = 0
        #     pCharSet = set(puzzle)
        #     for word in charSetDict[puzzle[0]]:
        #         if wordSubSetDict[word].issubset(pCharSet):
        #             subAns += 1
        #     ans.append(subAns)
        # return ans
