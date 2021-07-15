from collections import defaultdict

class ListNode:
    def __init__(self, x, n=None):
        self.val = x
        self.next = n

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.head = ListNode(kingName)
        
        self.d = defaultdict(list)
        self.dead_people = {'king':0}

    def birth(self, parentName: str, childName: str) -> None:
        
#         looking = parentName
#         while self.d[looking]:
#             looking = self.d[looking][-1]
        
#         # insert child into list
#         h = self.head
#         prev = h
#         while h != None:
#             prev = h
#             if h.val == looking:
#                 break
#             h = h.next
#         t = prev.next
#         prev.next = ListNode(childName, prev.next)
            
        self.d[parentName].append(childName)
        self.dead_people[childName] = 0

    def death(self, name: str) -> None:
        self.dead_people[name] = 1
        
    def df(self, name):
        
        l = []
        if self.dead_people[name] == 0:
            l.append(name)
        for childs in self.d[name]:
            l = l + self.df(childs)
            
        return l
        
    def getInheritanceOrder(self) -> List[str]:
        # ans = []
        # h = self.head
        # while h != None:
        #     if self.dead_people[h.val] == 0:
        #         ans.append(h.val)
        #     h = h.next
        # return ans
        return self.df('king')


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

