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


def getCCnt(w):
    cnt = {}
    for c in w:
        if not c in cnt:
            cnt[c] = 0
        cnt[c] += 1
    return cnt


class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        minCnt = {}
        for w in B:
            cToCnt = getCCnt(w)
            for c, cnt in cToCnt.items():
                if not c in minCnt:
                    minCnt[c] = 0
                minCnt[c] = max(minCnt[c], cnt)
        ans = []
        for w in A:
            cToCnt = getCCnt(w)
            good = 1
            for c, cnt in minCnt.items():
                if not (c in cToCnt and cToCnt[c] >= minCnt[c]):
                    good = 0
                    break
            if good:
                ans.append(w)
        return ans

\"\"\"
sol = Solution()
A = [\"amazon\", \"apple\", \"facebook\", \"google\", \"leetcode\"]
B = [\"e\", \"o\"]
B = [\"l\", \"e\"]
B = [\"e\", \"oo\"]
B = [\"lo\", \"eo\"]
B = [\"ec\", \"oc\", \"ceo\"]
print(sol.wordSubsets(A, B))
\"\"\"
