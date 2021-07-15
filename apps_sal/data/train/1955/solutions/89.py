class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        class UF:
            def __init__(self, n): self.p = list(range(n))
            # set one number's parent to other number's parent
            def union(self, x, y): self.p[self.find(x)] = self.find(y)
            # find current num's root node using recursive call 
            def find(self, x):
                if x != self.p[x]:
                    self.p[x] = self.find(self.p[x])
                return self.p[x]
        
        union_find, result, group = UF(len(s)), [], defaultdict(list)
        # join the groups
        for pair in pairs:
            union_find.union(pair[0], pair[1])
         
        #for i in range(len(s)):
        #    union_find.p[i] = union_find.find(i)
        # append list of num to the parent node 
        for i in range(len(s)):
            group[union_find.find(i)].append(s[i])
        # sort the keys in the group 
        for comp_id in list(group.keys()):
            group[comp_id].sort(reverse=True)
        # using pop to append
        for i in range(len(s)):
            result.append(group[union_find.find(i)].pop())
        return ''.join(result)

