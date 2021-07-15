class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        s = set()
        for a in A:
            s.add(''.join(sorted(a[::2])) + ''.join(sorted(a[1::2])))
        return len(s)
        
        
#         dic = Counter()
        
#         def idx(x):
#             ans = \"\"
#             for k in sorted(x):
#                 ans += k + str(x[k])
#             return ans
        
#         for a in A:
#             odd = Counter(a[1::2])
#             even = Counter(a[::2])
#             dic[idx(odd), idx(even)] += 1
            
#         return len(dic)
            
        
            
            

