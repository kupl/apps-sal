class Node:
    def __init__(self, val):
        self.val = val
        self.prev = self.next = self.up = self.down = None

class Skiplist:

    def __init__(self):
        self.heads = []
        self.tails = []
        self.newLevel()
        
    def newLevel(self):
        head = Node(float(\"-inf\"))
        tail = Node(float(\"inf\"))
        self.link_prev_next(head, tail)
        if self.heads:
            self.link_up_down(head, self.heads[-1])
            self.link_up_down(tail, self.tails[-1])
        self.heads.append(head)
        self.tails.append(tail)
        
    def find(self, num):
        node = self.heads[-1]
        tails = []
        while node:
            while node.next and num > node.next.val:
                node = node.next
            tails.append(node)
            node = node.down
        return tails

    def search(self, target: int) -> bool:
        return target == self.find(target)[-1].next.val

    def add(self, num: int) -> None:
        tails = self.find(num)
        left = tails.pop()
        node = Node(num)
        self.insert(left, left.next, node)
        while random.random() <= 0.5:
            new_node = Node(num)
            self.link_up_down(new_node, node)
            if not tails:
                self.newLevel()
                left = self.heads[-1]
            else:
                left = tails.pop()
            self.insert(left, left.next, new_node)
            node = new_node

    def erase(self, num: int) -> bool:
        node = self.find(num)[-1].next
        if node.val != num:
            return False
        while node:
            self.link_prev_next(node.prev, node.next)
            node = node.up
        return True
    
    def link_prev_next(self, node1, node2):
        node1.next = node2
        node2.prev = node1
    
    def link_up_down(self, node1, node2):
        node1.down = node2
        node2.up = node1
        
    def insert(self, left, right, node):
        self.link_prev_next(left, node)
        self.link_prev_next(node, right)
            

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
