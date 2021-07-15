# this is version after checking the discussions
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        class unionFind:
            def __init__(self, n):
                #here index = component id, initiallly point to eachself
                self.parents = list(range(n))
                
            def union (self, x, y):
                # make y's parent x's
                self.parents[self.find(x)] = self.find(y)
                
            def find (self, x):
                # parent's parent == themself
                # if this x is not a parent, find and record his final parent
                if self.parents[x]!=x: self.parents[x] = self.find(self.parents[x])
                return self.parents[x]
            
        uf1 = unionFind(len(s))
        
        for x,y in pairs:
            uf1.union(x,y)
        # every index of parents (implied index of s) found his parents now
        
        # because old parents won't be updated if their parent have a new parent
        # do find to all indices to make sure the parents list is clean
        for i in range(len(s)):
            uf1.find(i)
        
        groupList = defaultdict(list)
        
        # make indices with same parents group together, get char directly from string
        for i in range(len(s)):
            groupList[uf1.parents[i]].append(s[i])
        
        # sort each group (list), reversely
        for key in groupList.keys():
            groupList[key].sort(reverse = True)
        
        #pop out char from behind of each group
        result = []
        for i in range(len(s)):
            result.append(groupList[uf1.parents[i]].pop())
        
        # the way convert list to str
        return \"\".join(result)
        
        
