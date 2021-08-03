from collections import Counter


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        cnt, ans = Counter(), []

        for name in names:
            if name not in cnt:
                ans.append(name)
                cnt[name] += 1
            else:
                while name + '(' + str(cnt[name]) + ')' in cnt:
                    cnt[name] += 1
                ans.append(name + '(' + str(cnt[name]) + ')')
                cnt[name + '(' + str(cnt[name]) + ')'] += 1

        return ans
