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
\"\"\"
possible[weight][N] = possible[N - weight][N - 1], or 
\"\"\"


class Solution:

    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        left0i = [[-1 for _ in range(M)] for _ in range(N)]
        down0i = [[-1 for _ in range(M)] for _ in range(N)]

        for i in range(N):
            for j in range(M):
                if grid[i][j]:
                    if j:
                        left0i[i][j] = left0i[i][j - 1]
                else:
                    left0i[i][j] = j


#        print(left0i)

        for j in range(M):
            for i in range(N):
                if grid[i][j]:
                    if i:
                        down0i[i][j] = down0i[i - 1][j]
                else:
                    down0i[i][j] = i

        for l in range(min(M, N), 0, -1):
            for i in range(l - 1, N):
                for j in range(l - 1, M):
                    bottom = j - left0i[i][j]
                    top = j - left0i[i - l + 1][j]
                    left = i - down0i[i][j - l + 1]
                    size = min(bottom, i - down0i[i][j], left, top)
                    if size >= l:
                        return l * l
        return 0
