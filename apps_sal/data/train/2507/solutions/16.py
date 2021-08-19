class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        op = 0
        for ele in words:
            count = 0
            for i in set(ele):
                if chars.count(i) >= ele.count(i):
                    count += 1
            if count == len(set(ele)):
                op += len(ele)
        return op
