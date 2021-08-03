class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        flag = [0 for i in range(len(words))]
        total = 0

        for word in words:

            dic = {}

            for char in word:
                if char in dic:
                    dic[char] += 1
                else:
                    dic[char] = 1

            count = 0

            for i in range(len(chars)):
                if chars[i] in dic and dic[chars[i]] > 0:
                    dic[chars[i]] -= 1
                    count += 1

            good = True

            for char in dic:
                if dic[char] > 0:
                    good = False
                    break

            if good:
                total += count

        return total
