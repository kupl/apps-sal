class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        ans = [label]
        while label:
            llen = len(bin(label)[2:])
            label = ( pow(2, llen) -1 - label + pow(2, llen-1) ) // 2
            ans.append(label)
\t\t
        return ans[-2::-1]
        
