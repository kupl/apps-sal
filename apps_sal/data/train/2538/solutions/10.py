class Solution:
    def countLargestGroup(self, n: int) -> int:
        dic = defaultdict(list)
        max_ = 0
        for i in range(1, n + 1):
            result = 0
            num = i
            while i > 0:
                rem = i % 10
                result += rem
                i = int(i / 10)

            dic[result].append(num)

        max_ = 0
        for i in dic:
            leng = len(dic[i])
            max_ = max(max_, leng)

        ans = [dic[key] for key in dic if len(dic[key]) == max_]
        return len(ans)
