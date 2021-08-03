class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        was = set()
        cnt = dict()
        ans = []
        for s in names:
            if s not in was:
                was.add(s)
                cnt[s] = 1
                ans.append(s)
                continue
            if s not in cnt:
                cnt[s] = 1
            i = cnt[s]
            while (s + \"(\"+str(i)+\")\") in was:
                i += 1
            cnt[s] = i
            was.add(s + \"(\"+str(i)+\")\")
            ans.append(s + \"(\"+str(i)+\")\")
        
        return ans
