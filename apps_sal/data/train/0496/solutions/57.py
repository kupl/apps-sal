from typing import List
from collections import deque, Counter


class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        # print('-----')
        # print(f'A: {A}')

        cs = sorted([n, count] for n, count in list(Counter(A).items()))
        stack = deque(cs[::-1])
        # print(f'stack: {stack}')

        numOps = 0

        while stack:
            n, count = stack.pop()
            # print(f'n={n} count={count} numOps={numOps}', end=' ')
            numOps += count - 1
            if count > 1 and stack and stack[-1][0] == n + 1:
                stack[-1][1] += count - 1
                # print(f'move to {n+1, stack[-1][1]} stack={stack}')
            elif count > 1:
                stack.append([n+1, count-1])
                # print(f'upgrade to {n+1, count-1} stack={stack}')
            # else:
            #     print('')

        return numOps


