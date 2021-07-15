class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if len(dislikes) == 0:
            return True
        seenA = set()
        seenB = set()
        seen = set()
        ref = dict()
        stack = []
        for i in range(1, N+1):
            ref[i] = []
        for l in dislikes:
            s, t = l[0], l[1]
            ref[s].append(t)
            ref[t].append(s)
        erase = []
        for i in ref:
            if len(ref[i]) == 0:
                erase.append(i)
        for i in erase:
            ref.pop(i)
        stack = list(ref.keys())
        while len(stack) != 0:
            i = stack.pop(0)
            if i in seen:
                continue
            target = seenA if i in seenA else seenB
            other = seenB if i in seenA else seenA
            target.add(i)
            seen.add(i)
            for j in ref[i]:
                stack.insert(0, j)
                if j in target:
                    return False
                else:
                    other.add(j)
        return True
                
        
            

