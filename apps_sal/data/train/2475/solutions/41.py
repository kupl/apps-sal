class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        count=0
        for i in zip(*A):
            if ''.join(i)!=''.join(sorted(list(map(''.join,i)))):
                count+=1
        return count
