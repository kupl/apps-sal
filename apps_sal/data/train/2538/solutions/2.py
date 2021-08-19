class Solution:

    def countLargestGroup(self, n: int) -> int:
        dic = {}
        for i in range(1, n + 1):
            key = 0
            while i:
                key += i % 10
                i = i // 10
            dic[key] = dic.get(key, 0) + 1
        size = list(dic.values())
        return size.count(max(size))
