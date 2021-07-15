from math import floor
from math import ceil
from math import sqrt
from collections import deque
import numpy
from _collections import deque
#from _ast import Num # LC doesn't like this
from heapq import *
from typing import List
import random

MOD = int(1e9 + 7)
BASE = 256

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def match(head, root):
    if not head.next and root:
        return head.val == root.val
    elif not root:
        return 0
    return head.val == root.val and (match(head.next, root.left) or match(head.next, root.right))

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if not root:
            return 0
        return match(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right) 
        


\"\"\"
s = Solution()
n4 = TreeNode(4)
n3 = TreeNode(3, n4)
n2 = TreeNode(2, None, n3)
n4 = TreeNode(41)
n1 = TreeNode(1, n2, n4)
n5 = TreeNode(5)
n4 = TreeNode(4, None, n5)
n3 = TreeNode(3, n4)
n2 = TreeNode(2, None, n3)
n1 = TreeNode(1, None, n2)
print(s.longestZigZag(n1))
\"\"\"

