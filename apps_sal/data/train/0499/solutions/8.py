class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans=1
        target=target+[1]
        pre=1
        _max=1
        _min=10**9
        for i in range(len(target)-1):
            cur=target[i]
            if cur==1:continue
            nex=target[i+1]
            if cur<=nex:
                 if nex>_max:_max=nex
            else:
                if nex<_min:_min=nex
                if cur>_max:_max=cur
                ans+=min(_max-pre,_max-1)
                pre=_min
                _min=10**9
                _max=nex
        return ans        

