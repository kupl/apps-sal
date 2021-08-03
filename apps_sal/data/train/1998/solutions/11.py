class Solution:
    def __init__(self):
        self.GOAL_STATE = [1, 2, 3, 4, 5, 0]

    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        from itertools import chain
        seen = set()

        from collections import deque
        q = deque()
        q.append((list(chain.from_iterable(board)), 0))

        while q:
            state, dist = q.popleft()
            seen.add(tuple(state))

            if state == self.GOAL_STATE:
                return dist

            for nextState in self.nextStates(state):
                if tuple(nextState) not in seen:
                    q.append((nextState, dist + 1))

        return -1

    def swap(self, state, i, j):
        temp = state[i]
        state[i] = state[j]
        state[j] = temp

    def getNeighbors(self, index):
        neighbors = {0: [1, 3], 1: [0, 4, 2], 2: [1, 5], 3: [0, 4], 4: [3, 1, 5], 5: [4, 2]}
        return neighbors[index]

    def nextStates(self, state):
        states = []
        zeroIndex = state.index(0)

        for nei in self.getNeighbors(zeroIndex):
            nextState = list(state)
            self.swap(nextState, nei, zeroIndex)
            states.append(nextState)
        return states
