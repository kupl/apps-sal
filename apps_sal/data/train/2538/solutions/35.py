class Solution:
    def countLargestGroup(self, n: int) -> int:
        dic = {}
        for i in range(1, n + 1):
            s = sum([int(i) for i in str(i)])
            if s in dic:
                dic[s].append(i)
            else:
                dic[s] = [i]

        max_L = 0
        cnt = 0
        for j in dic:
            if len(dic[j]) == max_L:
                cnt += 1
            elif len(dic[j]) > max_L:
                cnt = 1
                max_L = len(dic[j])

        return cnt
