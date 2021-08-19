class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        n = len(chars)
        for word in words:
            ok_word = True
            copy = chars
            visit = []
            for i in range(n):
                visit.append(0)
            for letter in word:
                ok_letter = False
                for i in range(n):
                    if visit[i] == 0 and letter == copy[i]:
                        ok_letter = True
                        visit[i] = 1
                        break
                if not ok_letter:
                    ok_word = False
                    break
            if ok_word:
                count += len(word)
        return count
