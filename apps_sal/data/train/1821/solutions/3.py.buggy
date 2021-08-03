class Node:
    def __init__(self, val):
        self.val = val
\t
\t# lt means less than, le means less or equal than etc.
    def __lt__(self, other):
        return self.val < other.val
    
class Solution:    
    def sortArray(self, nums: List[int]) -> List[int]:
        nodes = [Node(n) for n in nums]
        return [node.val for node in sorted(nodes)]
