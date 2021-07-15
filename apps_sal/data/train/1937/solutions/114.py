class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king_name =kingName
        self.inheritance_tree = {
            kingName:{
                \"children\":[],
                \"death\" : False
            },
            
        }

    def birth(self, parentName: str, childName: str) -> None:
        self.inheritance_tree[parentName][\"children\"].append(childName)
        self.inheritance_tree[childName] = {
                \"children\":[],
                \"death\" : False
        }

    def death(self, name: str) -> None:
        self.inheritance_tree[name][\"death\"] = True
        


    def getInheritanceOrder(self) -> List[str]:
        
        res = []
        def helper(person,res):
            # print(self.inheritance_tree[person][\"children\"])
            if self.inheritance_tree[person][\"death\"] == False:
                res.append(person)

            if len(self.inheritance_tree[person]) == 0:
                return 

            for child in self.inheritance_tree[person][\"children\"]:
                helper(child,res)
        
        helper(self.king_name, res)

        return res


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
