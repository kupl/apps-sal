class ListNode:
    
    def __init__(self, val):
        self.val = val
        self.next = None
        self.down = None


class Skiplist:

    def __init__(self):
        self.levels = []
        
        # Because the number of calls is <50000, and 2^16>60000, which is enough to handle all calls.
        # Otherwise we need to consider the situation new level need to be added when level not being enough.
        vertical = None
        for _ in range(16):
            head = ListNode(float(\"-inf\"))  # 新建一些dummyhead放到每一层的头部
            self.levels.append(head)        # 处理each level - horizontal
            if vertical:                        # 处理verticals
                vertical.down = head
            vertical = head
            
    def _find_smaller(self, target):
        \"\"\"
        helper function to find the largest node that is smaller than search target in EACH levels
        and store them in a list, return the list
        \"\"\"
        res = []
        
        curr = self.levels[0]
        while curr:
            while curr.next and curr.next.val < target:
                curr = curr.next
            res.append(curr)    # on each level, just append the largest node that is smaller than target
            
            curr = curr.down
            
        return res

    def search(self, target: int) -> bool:
        last = self._find_smaller(target)[-1]   # last is just smaller node on the last level
        if last.next and last.next.val == target:
            return True
        return False

    def add(self, num: int) -> None:
        smaller = self._find_smaller(num) # the idea is to insert a new_node at the right place, we find the right place at each level first
        vertical = None
        for node in smaller[::-1]:      # If we add a node in a level, all levels after that also need to be added, so loop reversely
            new_node = ListNode(num)    # the idea is to insert a new_node at the right place, we create a new node first
            
            # firstly, insert the new_node to the level - horizontal
            new_node.next = node.next
            node.next = new_node
            
            # then, point the new_node.down to it's corresponding down node - vertical
            new_node.down = vertical
            vertical = node
            
            # we don't insert the new_node to every level, we only inser the new_node to some levesl on the bottom
            # how to we decide which levels to insert? we use coin toss
            # The purpose of coin toss is to ensure that each node at current level will be 
            # duplicated to its upper level with a probability of 0.5, 
            # so the number of nodes at the upper level is roughly half of the current level.
            # So in the extreme case, SkipList is equivalent to a balanced binary search tree.
            # that is why add, erase and search can be O(logn)
            rand = random.randrange(0, 10)
            if rand >= 5:   # half of the possibility that we stop inserting the new_node to any upper levels
                break

    def erase(self, num: int) -> bool:
        smaller = self._find_smaller(num)
        found = False
        for node in smaller[::-1]:
            while node.next:
                if node.next.val == num:
                    node.next = node.next.next  # remove the node
                    found = True
                    break
                node = node.next
            if not node.next:   # 如果这一层都找不到num, 那上面的level更找不到了
                break
        return found


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
