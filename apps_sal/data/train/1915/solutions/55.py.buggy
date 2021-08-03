class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        res = []
        ns,nt = len(stamp),len(target)
        final = \"?\"*nt
        def same(ind):
            other = False
            for i in range(ns):
                if target[i+ind] not in stamp[i]+\"?\":
                    return False
                if target[i+ind]!=\"?\":
                    other = True
            return other
        change = True
        while change:
            change = False
            for ind in range(nt-ns+1):
                if same(ind):
                    change=True
                    res.append(ind)
                    target=target[:ind]+\"?\"*ns+target[ind+ns:]
        return res[::-1] if all(i==\"?\" for i in target) else []
