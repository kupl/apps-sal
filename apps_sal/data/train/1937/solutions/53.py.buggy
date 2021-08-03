
class ThroneInheritance:
    
    def __init__(self, kingName: str):
        self.dic = dict()
        self.king = kingName
        self.dic[\"1_\"+kingName] = dict()
        self.direct = {kingName:self.dic[\"1_\"+kingName]}
        self.dead = set()
        

    def birth(self, parentName: str, childName: str) -> None:
        #名字上面加当前层的顺序
        if parentName in self.dead:
            return
        if parentName not in self.direct:
            return
        
        cur_dic = self.direct[parentName]
        order = str(len(cur_dic)+1) + \"_\"
        cur_dic[order + childName] = dict()
        self.direct[childName] = cur_dic[order + childName]

    def death(self, name: str) -> None:
        if name not in self.direct:
            return
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        res = []
            
        def compare1(s1, s2):
            s1 = int(s1.split(\"_\")[0])
            s2 = int(s2.split(\"_\")[0])
            if s1 < s2:
                return -1
            elif s1 > s2:
                return 1
            return 0
        def recur(parent):
            if parent not in self.dead:
                res.append(parent)
            cd = self.direct[parent]
            if len(cd) > 0:
                keys = sorted(list(cd.keys()), key=functools.cmp_to_key(compare1))
                # if parent == \"theresa\":
                    # print(parent, \"-\", keys)
                for c in keys:
                    c = c.split(\"_\")[1]
                    recur(c)
                    
        recur(self.king)
        return res
            


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
