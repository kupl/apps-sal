class Solution:
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        from collections import deque as dq
        curs = "".join(map(str, board[0])) + "".join(map(str, board[1]))
        dist, pre = {}, {}
        dist[curs] = 0
        q = dq([curs])
        while q:
            curs = q.pop()
            if curs == "123450":
                while curs in pre:
                    # print(curs)
                    curs = pre[curs]
                return dist["123450"]
            #print("curs is" + curs, curs not in dist)
            ind = curs.index("0")
            if ind > 0 and ind != 3:
                preswap = curs[:ind - 1] + '0' + curs[ind - 1] + curs[ind + 1:]
                #print("preswap is" + preswap)
                if preswap not in dist:
                    dist[preswap] = dist[curs] + 1
                    pre[preswap] = curs
                    q.appendleft(preswap)
            if ind < 5 and ind != 2:
                afterswap = curs[:ind] + curs[ind + 1] + '0' + curs[ind + 2:]
                #print("afterswap is" + afterswap)
                if afterswap not in dist:
                    dist[afterswap] = dist[curs] + 1
                    pre[afterswap] = curs
                    q.appendleft(afterswap)
            if ind < 3:
                downswap = curs[:ind] + curs[ind + 3] + curs[ind + 1:ind + 3] + '0' + curs[ind + 4:]
                #print("downswap is" + downswap)
                if downswap not in dist:
                    dist[downswap] = dist[curs] + 1
                    pre[downswap] = curs
                    q.appendleft(downswap)
            else:
                upswap = curs[:ind - 3] + '0' + curs[ind - 2:ind] + curs[ind - 3] + curs[ind + 1:]
                #print("upwap is" + upswap)
                if upswap not in dist:
                    dist[upswap] = dist[curs] + 1
                    pre[upswap] = curs
                    q.appendleft(upswap)
            # print(dist)

        return -1
