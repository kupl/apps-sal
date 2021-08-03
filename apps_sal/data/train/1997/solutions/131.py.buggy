from heapq import heapify, heappush, heappop
START = 0 
END = 1

class BinaryTreeNode(object):
    __slots__ = [\"val\", \"left\", \"right\", \"parent\", \"height\"]
    def __init__(self, val, parent=None):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
        self.parent = parent
        
    def min(self):
        node = self
        while node.left:
            node = node.left
        return node.val
        
    def setHeight(self):
        lh = self.left.height if self.left else 0
        rh = self.right.height if self.right else 0
        self.height = 1 + max(lh, rh)
        
    def balanceF(self):
        lh = self.left.height if self.left else 0
        rh = self.right.height if self.right else 0
        return lh - rh
    
    def nextNode(self):
        isLeft = lambda c: c.parent and c.parent.left is c
        
        current = self
        if current.right:
            current = current.right
            while current.left:
                current = current.left
            return current
        else:
            while current.parent and not isLeft(current):
                current = current.parent
            return current.parent
            
    def prevNode(self):
        isLeft = lambda c: c.parent and c.parent.left is c
        
        current = self
        if current.left:
            current = current.left
            while current.right:
                current = current.right
            return current
        else:
            while current.parent and isLeft(current):
                current = current.parent
            return current.parent

    def validate(self,min_value=None, max_value=None):
        if min_value is not None:
            if self.val < min_value:
                print(\"bad_node\")
                return False
        if max_value is not None:
            if self.val > max_value:
                print(\"bad_node\")
                return False

        l, r = True, True
        if self.left:
            l = self.left.parent is self and self.left.validate(min_value, self.val)
        if self.right:
            r = self.right.parent is self and self.right.validate(self.val, max_value)
        
        return l and r
        

class AvlTree(object):
    __slots__ = [\"root\", \"size\", \"min\"]
    def __init__(self):
        self.root = None
        self.size = 0
        self.min = None
        
    def add(self, val, node=None):
        if not self.root:
            self.root = BinaryTreeNode(val)
            self.size += 1
            return self.root
        
        if node is None:
            node = self.root
            
        if val < node.val:
            if node.left:
                added = self.add(val, node.left)
            else:
                node.left = BinaryTreeNode(val, node)
                self.size += 1
                added = node.left  
        else:
            if node.right:
                added = self.add(val, node.right)
            else:
                node.right = BinaryTreeNode(val, node)
                self.size += 1
                added = node.right 
    
        node.setHeight()
        self.balance(node)
        if self.min is None or self.min > val:
            self.min = val
        return added
        
    def balance(self, node):
        if node.balanceF() > 1:
            if node.left.balanceF() > 0:
                self.rotateRight(node)
            else:
                self.rotateLeft(node.left)
                self.rotateRight(node)
        elif node.balanceF() < -1:
            if node.right.balanceF() < 0:
                self.rotateLeft(node)
            else:
                self.rotateRight(node.right)
                self.rotateLeft(node)

    def swapNodes(self, nodeA, nodeB):
        if nodeA.parent is nodeB:
            return self.swapNodes(nodeB, nodeA)
            
        a_p, a_l, a_r, a_h = nodeA.parent, nodeA.left, nodeA.right, nodeA.height
        b_p, b_l, b_r, b_h = nodeB.parent, nodeB.left, nodeB.right, nodeB.height

        nodeA.parent, nodeA.left, nodeA.right, nodeA.height = b_p, b_l, b_r, b_h
        nodeB.parent, nodeB.left, nodeB.right, nodeB.height = a_p, a_l, a_r, a_h

   
        if nodeA.left is nodeA:
            nodeA.left = nodeB
        elif nodeA.right is nodeA:
            nodeA.right = nodeB
        if nodeB.left is nodeB:
            nodeB.left = nodeA
        elif nodeB.right is nodeB:
            nodeB.right = nodeA
        if nodeA.right:
            nodeA.right.parent = nodeA
        if nodeA.left:
            nodeA.left.parent = nodeA
        if nodeB.right:
            nodeB.right.parent = nodeB
        if nodeB.left:
            nodeB.left.parent = nodeB

        if nodeA.parent is None:
            self.root = nodeA
        elif nodeA.parent.left is nodeB:
            nodeA.parent.left = nodeA
        else:
            nodeA.parent.right = nodeA
        if nodeB.parent is None:
            self.root = nodeB
        elif nodeB.parent.left is nodeA:
            nodeB.parent.left = nodeB
        else:
            nodeB.parent.right = nodeB
            
                
    def remove(self, node):
        self.size -= 1
        while node.left or node.right:
            replace = None
            if not node.right:
                replace = node.left
            elif not node.left:
                replace = node.right
            if replace:
                if node.parent is None:
                    self.root = replace
                elif node.parent.left is node:
                    node.parent.left = replace
                else:
                    node.parent.right = replace
                replace.parent = node.parent
                node.parent = replace
                break
            else:
                swap = node.nextNode()
                self.swapNodes(node, swap)
            
        if node.parent is None:
            self.root = None
        else:
            if node.parent.left is node:
                node.parent.left = None
            elif node.parent.right is node:
                node.parent.right = None
            
        current = node.parent
        while current:
            current.setHeight()
            #self.balance(current)
            current = current.parent
        if self.size == 0:
            self.min = None
        elif node.val == self.min:
            self.min = self.root.min()
                
                
    def setParent(self, parent, new_node):
        if parent is None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node
        new_node.parent = parent
        
    def rotateLeft(self, node):
        nr = node.right
        node.right = nr.left
        if nr.left:
            nr.left.parent = node
        nr.left = node
        old_parent = node.parent
        node.parent = nr
        self.setParent(old_parent, nr)
        node.setHeight()
        nr.setHeight()
        
    def rotateRight(self, node):
        nl = node.left
        node.left = nl.right
        if nl.right:
            nl.right.parent = node
        nl.right = node
        old_parent = node.parent
        node.parent = nl
        self.setParent(old_parent, nl)
        node.setHeight()
        nl.setHeight()        
    
    def __len__(self):
        return self.size
    
    
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        events = [(a[0], START, -a[1] , i) for i, a in enumerate(intervals)]
        events.extend([(a[1], END, -a[0] , i) for i, a in enumerate(intervals)])
        events.sort()
        
        tree = AvlTree()
        nodes = [None]*len(intervals)
        answer = len(intervals)
        while len(events) > 0:
            event = heappop(events)
            if event[1] == START:
                nodes[event[3]] = tree.add(event[0])
            else:
                tree.remove(nodes[event[3]])
                #print(tree.min)
                if tree.min is not None and tree.min <= intervals[event[3]][0]:
                    #print(event)
                    answer -= 1
        return answer
                
                
            
            
            
        
