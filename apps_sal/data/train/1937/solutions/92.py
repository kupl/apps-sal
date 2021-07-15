class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = kingName
        self.child_list = {
            self.root: []
        }
        self.death_dict = {}
        

    def birth(self, parentName: str, childName: str) -> None:
        self.child_list[parentName].append(childName)
        self.child_list[childName] = []
        

    def death(self, name: str) -> None:
        self.death_dict[name] = True

    def getInheritanceOrder(self) -> List[str]:
        answer_list = []
        def _dfs(cur_node):
            if cur_node not in self.death_dict:
                answer_list.append(cur_node)
            for child in self.child_list[cur_node]:
                _dfs(child)
        _dfs(self.root)
        return answer_list


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

