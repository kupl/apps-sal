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


def split(f1, f2, si, S):
    N = len(S)
    if N <= si:
        return []
    prefixNum = f1 + f2
    if prefixNum >= (1 << 31):
        return []
    prefixS = str(f1 + f2)

    if S[si] == '0':
        if prefixNum > 0:
            return []
        else:
            if si == N - 1:
                return [0]
            else:
                tail = split(f2, 0, si + 1, S)
                if len(tail):
                    tail.append(0)
                    return tail
                else:
                    return []

    else:
        nextSi = si + len(prefixS)
        if nextSi <= N and S[si:nextSi] == prefixS:
            if nextSi == N:
                return [prefixNum]
            else:
                #print(\"split!!\")
                tail = split(f2, prefixNum, si + len(prefixS), S)
                if len(tail):
                    tail.append(prefixNum)
                    return tail
    return []


class Solution:

    def splitIntoFibonacci(self, S: str) -> List[int]:
        N = len(S)
        for firstEI in range(N - 2):
            if S[0] == '0' and firstEI > 0:
                continue
            firstN = int(S[:firstEI + 1])
            for secondEI in range(firstEI + 1, N - 1):
                if S[firstEI + 1] == '0' and secondEI > firstEI + 1:
                    continue
                secondN = int(S[firstEI + 1:secondEI + 1])

                tail = split(firstN, secondN, secondEI + 1, S)
                if len(tail):
                    tail.reverse()
                    ans = [firstN, secondN]
                    ans.extend(tail)
                    return ans

        return []

\"\"\"
S = Solution()
s = \"123456579\"
s = \"112358130\"
s = \"0123\"
s = \"011\"
s = \"0123\"
s = \"11235813\"
s = \"1101111\"
s = \"0000\"
print(S.splitIntoFibonacci(s))
\"\"\"

