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

def dfs(root, rv, s):
    if not root:
        return
    s.add(rv)
    dfs(root.left, 2 * rv + 1, s)
    dfs(root.right, 2 * rv + 2, s)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        self.s = set()
        dfs(root, 0, self.s)

    def find(self, target: int) -> bool:
        return target in self.s


\"\"\"
\"\"\"
