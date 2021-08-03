class ThroneInheritance:
    from collections import deque

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.dic = {kingName: [1, []]}

    def birth(self, parentName: str, childName: str) -> None:
        self.dic[parentName][1].append(childName)
        self.dic[childName] = [1, []]

    def death(self, name: str) -> None:
        self.dic[name][0] = 0

    def getInheritanceOrder(self) -> List[str]:
        d = deque([self.kingName])
        ans = []
        while len(d) > 0:
            name = d.pop()
            if self.dic[name][0]:
                ans.append(name)
            listt = self.dic[name][1]
            for i in range(len(listt)):
                d.append(listt[-i - 1])

        return ans
