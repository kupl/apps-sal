class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        full = set()
        priority = []
        toReturn = []
        for i in rains:
            if i != 0:
                if i in full:
                    priority.append(i)
                else:
                    full.add(i)
        full = set()
        for i in rains:
            if i == 0:
                done = False
                for x in range(len(priority)):
                    if priority[x] in full:
                        a = priority.pop(x)
                        toReturn.append(a)
                        full.remove(a)
                        done = True
                        break
                if not done:
                    toReturn.append(1)
            elif i in full:
                return []
            else:
                full.add(i)
                toReturn.append(-1)
        return toReturn
