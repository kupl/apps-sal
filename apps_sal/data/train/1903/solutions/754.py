class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 2:
            return abs(points[0][0] - points[1][0]) + abs(points[1][1] - points[0][1])
        if len(points) == 1:
            return 0
        connSet = set()
        unConnSet = set()
        for i in range(len(points)):
            unConnSet.add(i)
        myHeap = []
        for i in range(len(points)):
            for j in range(i):
                lenCalc = abs(points[i][0] - points[j][0]) + abs(points[j][1] - points[i][1])
                if lenCalc > 0:
                    myHeap.append([lenCalc, (i, j)])
        myHeap.sort(key=lambda x: x[0])
        p1 = myHeap[0][1][0]
        p2 = myHeap[0][1][1]
        connSet.add(p1)
        connSet.add(p2)
        unConnSet.remove(p1)
        unConnSet.remove(p2)
        itt = 0
        res = myHeap[0][0]
        myHeap.pop(0)
        while itt < len(myHeap) and len(unConnSet) > 0:
            p1 = myHeap[itt][1][0]
            p2 = myHeap[itt][1][1]
            if p1 in connSet and p2 not in connSet:
                connSet.add(p2)
                unConnSet.remove(p2)
                res += myHeap[itt][0]
                myHeap.pop(itt)
                itt = -1
            if p2 in connSet and p1 not in connSet:
                connSet.add(p1)
                unConnSet.remove(p1)
                res += myHeap[itt][0]
                myHeap.pop(itt)
                itt = -1
            itt += 1
        return res
