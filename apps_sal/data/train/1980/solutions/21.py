class LinkedList:
    
    def __init__(self, val):
        self.val = val
        self.next = None
        self.down = None


class Skiplist:

    def __init__(self):
        self.levels = [LinkedList(-1) for _ in range(20)]
        for u, d in zip(self.levels[:-1], self.levels[1:]):
            u.down = d

    def search(self, target: int) -> bool:
        pointer = self.levels[0]
        while pointer:
            if pointer.__next__ != None and pointer.next.val < target:
                pointer = pointer.__next__
            elif pointer.__next__ != None and pointer.next.val == target:
                return True
            else:
                pointer = pointer.down
        return False

    def add(self, num: int) -> None:
        stack = []
        pre = None
        pointer = self.levels[0]
        
        while pointer:
            if pointer.__next__ != None and pointer.next.val <= num:
                pointer = pointer.__next__
            else:#if pointer.next != None and pointer.next.val > target:
                stack.append(pointer)
                pointer = pointer.down
        while stack:
            pointer = stack.pop(-1)
            newNode = LinkedList(num)
            newNode.next, pointer.next = pointer.next, newNode
            if pre:
                newNode.down = pre
            pre = newNode
            if random.randrange(2): break

    def erase(self, num: int) -> bool:
        found = False
        pointer = self.levels[0]
        while pointer:
            if pointer.__next__ != None and pointer.next.val < num:
                pointer = pointer.__next__
            elif pointer.__next__ != None and pointer.next.val == num:
                pointer.next = pointer.next.__next__
                found = True
                pointer = pointer.down
            else:
                pointer = pointer.down
        return found


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)

