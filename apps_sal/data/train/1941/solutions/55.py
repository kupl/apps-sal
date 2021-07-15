class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        mp = defaultdict(int)
        for w in words:
            mask = 0
            for c in w:
                mask |= (1<<(ord(c)-ord('a')))

            mp[mask]+=1
        # print(mp)
        res = []
        for p in puzzles:
            lenp = len(p)-1
            cnt = 0
            for i in range(1<<lenp):
                mask = 1<<(ord(p[0])-ord('a'))
                for j in range(lenp):
                    if i & (1<<j):
                        mask|=(1<<(ord(p[j+1])-ord('a')))

                # print('mp', mp, 'mask', mask)
                if mp[mask]:
                    cnt+=mp[mask]


            res.append(cnt)

        return res

        
#         res = [0]*len(puzzles)
#         lswords = [set()]*len(words)
#         for idx, word in enumerate(words):
#             lswords[idx] = set(word)
      
#         # print('lisr of set words',lswords)
#         for idx, puzzle in enumerate(puzzles):
#             firstLetter = puzzle[0]
#             remLetters = set(puzzle)

#             cnt = 0
#             # print(puzzle, firstLetter, remLetters)
#             for sWord in lswords:
#                 # print(word, 'sword',sWord,'\
')
#                 if firstLetter in sWord and sWord.issubset(remLetters):
#                     # print('inc')
#                     cnt+=1

#             res[idx]=cnt
#             # print('end of puzzle\
\
')
#         return res

