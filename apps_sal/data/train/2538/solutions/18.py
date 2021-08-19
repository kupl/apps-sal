class Solution:
    def countLargestGroup(self, n: int) -> int:
        from collections import Counter
        al = [list(str(i)) for i in range(1, n + 1)]
        al = [sum([int(j) for j in i]) for i in al]
        col = Counter(al)
        # print(col)
        num = Counter(col.values())
        # print(num)
        return num[max(num.keys(), key=lambda x:x)]
