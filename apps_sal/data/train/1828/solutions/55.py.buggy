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
\"\"\"
startSI
nextSI
totalUsed

curEnd = si + (cnt - 1) * (m+1)
if curEnd >= nextSI:
    nextSI = curEnd + 1

if startSI

totalUsed += cnt

123123144 -> 143124123 -> 12312412455
14312412355


\"\"\"

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


class Solution:

    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        h = []
        N = len(barcodes)
        ans = []
        cnts = {}
        for c in barcodes:
            if not c in cnts:
                cnts[c] = 0
            cnts[c] += 1
        for c, cnt in cnts.items():
            heappush(h, (-cnt, c))
        while len(h):
            negCnt, c = heappop(h)
            if len(ans) and c == ans[-1]:
                negCnt2, c2 = heappop(h)
                ans.append(c2)
                newCnt2 = -negCnt2 - 1
                if newCnt2:
                    heappush(h, (-newCnt2, c2))
                heappush(h, (negCnt, c))
            else:
                ans.append(c)
                newCnt = -negCnt - 1
                if newCnt:
                    heappush(h, (-newCnt, c))
        return ans

\"\"\"
S = Solution()
l = [1, 1, 1, 2, 2, 2]
l = [1, 1, 1, 1, 2, 2, 3, 3]
print(S.rearrangeBarcodes(l))
\"\"\"
