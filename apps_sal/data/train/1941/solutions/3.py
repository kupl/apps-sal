class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        # TLE
        #bitWords = []
        # for word in words:
        #    n = 0
        #    for w in word:
        #        n = n | 1 << (ord(w) - ord('a'))
        #    bitWords.append(n)
        #
        #result = []
        # for puzzle in puzzles:
        #    n = 0
        #    f = 0
        #    for p in puzzle:
        #        n = n | 1 << (ord(p) - ord('a'))
        #    f = 1 << (ord(puzzle[0]) - ord('a'))
        #    cnt = 0
        #    for i in range(len(bitWords)):
        #        w = bitWords[i]
        #        if f & w and not (n & w)^w:
        #            cnt += 1
        #    result.append(cnt)
        # return result

        # TLE
        # 중복이 많이 개선됨
        count = collections.Counter()
        for word in words:
            n = 0
            for w in word:
                n = n | 1 << (ord(w) - ord('a'))
            count[n] += 1

        result = []
        for puzzle in puzzles:
            bfs = [1 << (ord(puzzle[0]) - 97)]
            m = 0
            # 모든 조합 찾기
            for p in puzzle[1:]:
                bfs += [m | 1 << (ord(p) - 97) for m in bfs]

            # 결과
            result.append(sum(count[m] for m in bfs))
        return result

        # 604
        #count = collections.Counter()
        # for w in words:
        #    if len(set(w)) > 7: continue
        #    m = 0
        #    for c in w:
        #        m |= 1 << (ord(c) - 97)
        #    count[m] += 1
        #
        #res = []
        # for p in puzzles:
        #    bfs = [1 << (ord(p[0]) - 97)]
        #    for c in p[1:]:
        #        bfs += [m | 1 << (ord(c) - 97) for m in bfs]
        #        print(bfs)
        #    res.append(sum(count[m] for m in bfs))
        # return res
