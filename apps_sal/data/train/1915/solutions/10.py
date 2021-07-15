class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        n = len(target)
        m = len(stamp)
        seen = [0]*n
        t = list(target)
        total = 0
        def match(ind): # to match pattens in target
            l = 0
            size = 0
            while l <=m-1 and ind+l<=n-1:
                if t[ind+l] == stamp[l]:
                    l+=1
                    size += 1
                elif t[ind+l]=='*':
                    l+=1
                else:
                    return 0
            t[ind:ind+l] = ['*']*l
            return size
        ans = []
        while total<n:
            found = False
            for i in range(n-m+1):
                if seen[i]==0:
                    num = match(i)
                    if num>0:
                        found = True
                        seen[i]=1
                        total+= num
                        ans.append(i)
                        break
            if found == False:
                break
        return ans[::-1] if total==n else []
