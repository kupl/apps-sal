class ThroneInheritance:

    def __init__(self, kingName: str):
        self.res = ['king']
        self.ex = {}
        self.par = {}
        self.child = {}

    def birth(self, pN: str, cN: str) -> None:
        self.child[cN] = pN
        if pN in self.par:
            # print(self.par)
            self.par[pN].append(cN)
        else:
            self.par[pN] = deque([cN])
        # print(self.par)

    def death(self, name: str) -> None:
        self.ex[name] = True

    def getInheritanceOrder(self) -> List[str]:
        final = []
        res = self.main()
        for i in res:
            if i not in self.ex:
                final.append(i)
        # self.res=final
        return final

    def main(self):
        # cP=self.par.deepcopy()
        cC = self.child.copy()
        cP = copy.deepcopy(self.par)
        # print(cP, cC)
        # cP={}
        # for i in self.par:
        #     cP[i]=self.par[i]
        # print(cP)

        res = ['king']
        curr = res[-1]

        while(True):
            if curr in cP and len(cP[curr]) > 0:
                res.append(cP[curr][0])
                cP[curr].popleft()
                curr = res[-1]
            else:
                if curr not in cC:
                    return res
                curr = cC[curr]
            if curr == 'king' and len(cP[curr]) == 0:
                # print(self.par, cP)
                return res

        # return final


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
