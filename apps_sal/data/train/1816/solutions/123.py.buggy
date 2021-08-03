class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        seen=collections.defaultdict(list)
        ans=[]
        for i in range(len(keyName)):
            h,m=map(int,keyTime[i].split(\":\"))
            seen[keyName[i]].append((60*h)+m)
        #print()
        for name in seen:
            seen[name].sort()
            l,r,n,found=0,0,len(seen[name]),False
            #print(name,seen[name])
            while l<n:
                if r+1<n and seen[name][r+1]-seen[name][l]<=60:
                    r+=1
                    if (r-l)+1>=3:
                        ans.append(name)
                        found=True
                        break
                else:
                    l+=1
        return sorted(ans)
