class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        originBridge = []

        def markBridge(cord):
            x = cord[1]
            y = cord[0]
            A[y][x] = 2
            originBridge.append(cord)

            if x < len(A[y]) - 1:
                if A[y][x + 1] == 1:
                    markBridge((y, x + 1))
            if x > 0:
                if A[y][x - 1] == 1:
                    markBridge((y, x - 1))
            if y < len(A) - 1:
                if A[y + 1][x] == 1:
                    markBridge((y + 1, x))
            if y > 0:
                if A[y - 1][x] == 1:
                    markBridge((y - 1, x))
        for y in range(len(A)):
            for x in range(len(A[y])):
                if A[y][x] == 1:
                    markBridge((y, x))
                    break
            if len(originBridge) > 0:
                break
        moves = 0
        bridgeList = set(originBridge)
        while len(originBridge) > 0:
            newMoves = []
            for b in originBridge:
                y = b[0]
                x = b[1]
                if x > 0:
                    if (y, x - 1) not in bridgeList:
                        if A[y][x - 1] == 1:
                            return moves
                        else:
                            bridgeList.add((y, x - 1))
                            newMoves.append((y, x - 1))
                if x < len(A[y]) - 1:
                    if (y, x + 1) not in bridgeList:
                        if A[y][x + 1] == 1:
                            return moves
                        else:
                            bridgeList.add((y, x + 1))
                            newMoves.append((y, x + 1))
                if y > 0:
                    if (y - 1, x) not in bridgeList:
                        if A[y - 1][x] == 1:
                            return moves
                        else:
                            bridgeList.add((y - 1, x))
                            newMoves.append((y - 1, x))
                if y < len(A) - 1:
                    if (y + 1, x) not in bridgeList:
                        if A[y + 1][x] == 1:
                            return moves
                        else:
                            bridgeList.add((y + 1, x))
                            newMoves.append((y + 1, x))
            originBridge = newMoves
            moves += 1
        return moves
