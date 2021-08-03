class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        self.table = {}
        res = []
        for name in names:
            if name in self.table:
                suffix = self.getSuffix(name)
                name += suffix
            res.append(name)
            self.putName(name)
        return res
    
    def getSuffix(self,name: str) -> str:
        counter,table = self.table[name]
        if counter == 0:
            return \"\"
        while counter in table:
            counter += 1
        self.table[name] = (counter+1,table)
        return \"(\" + str(counter) + \")\"
        
    def putName(self,name: str):
        if name[-1] == \")\":
            index = len(name)-2
            num = 0
            multiplier = 1
            while index >= 0 and str.isdigit(name[index]):
                num += multiplier * int(name[index])
                multiplier *= 10
                index -= 1
            if name[index] == \"(\":
                #perform table update
                if name[:index] in self.table:
                    c,table = self.table[name[:index]]
                    table.add(num)
                else:
                    a = set()
                    a.add(num)
                    self.table[name[:index]] = (0,a)
        if name in self.table:
            counter,table = self.table[name]
            self.table[name] = (counter+1,table)
        else:
            self.table[name] = (1,set())
