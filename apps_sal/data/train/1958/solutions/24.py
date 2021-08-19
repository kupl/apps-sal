class Solution:

    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        l = len(groupSizes)
        key = {}
        ans = []
        for i in range(l):
            now = groupSizes[i]
            if now not in key.keys():
                key[now] = []
                key[now].append(i)
            elif len(key[now]) != now:
                key[now].append(i)
            else:
                ans.append(key[now])
                key[now] = []
                key[now].append(i)
        for i in key.keys():
            if key[i] not in ans:
                ans.append(key[i])
                continue
        return ans
