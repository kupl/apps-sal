class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        pairs = {}
        for a,b in dislikes:
            if not a in pairs:
                pairs[a] = set()
            if not b in pairs:
                pairs[b] = set()
            pairs[a].add(b)
            pairs[b].add(a)
        seen = set()
        for i in range(1,N+1):
            if i in seen:
                continue
            curr = set([i])
            A, B = set(), set()
            A.add(i)
            flag = 1
            while len(curr):
                _next = set()
                for c in curr:
                    if c not in pairs:
                        continue
                    for n in pairs[c]:
                        if flag == 1 and n in A:
                            return False
                        if flag == 0 and n in B:
                            return False
                        if n in seen:
                            continue
                        if flag:
                            B.add(n)
                        else:
                            A.add(n)
                        seen.add(n)
                        _next.add(n)
                curr = _next
                flag ^= 1
        return True
                
                

