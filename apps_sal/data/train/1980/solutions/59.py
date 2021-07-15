import random
class Node(object):
    def __init__(self, val, right, down, left=None):
        self.val = val
        self.right = right
        self.down = down
        self.left = left
    
    def delete(self):
        self.left.right = self.right
        self.right.left = self.left
        
    def insert(self, val, down):
        node = Node(val, self.right, down, self)
        self.right.left = node
        self.right = node
        return node
        

class Skiplist(object):

    def __init__(self):
        end = Node(20001, None, None)
        self.head = Node(-1, end, None)
        end.left = self.head

    def addLayer(self):
        end = Node(20001, None, None)
        self.head = Node(-1, end, self.head)
        end.left = self.head
        
    def printList(self):
        print(\"=========\")
        #res = []
        head = self.head
        while head is not None:
            line = []
            cur = head
            while cur is not None:
                line.append(cur.val)
                cur = cur.right
            print(line)
            head = head.down
        
        
    def search(self, target):
        \"\"\"
        :type target: int
        :rtype: bool
        \"\"\"
        cur = self.head
        while cur is not None:
            if cur.right.val > target:
                cur = cur.down
            elif cur.right.val == target:
                return True
            else: # cur.next is not None and cur.next.val < target
                cur = cur.right
                
        return False
                

    def add(self, num):
        \"\"\"
        :type num: int
        :rtype: None
        \"\"\"
        cur = self.head
        
        stack = []
        
        while True:
            if cur.right.val <= num:
                cur = cur.right
            elif cur.down is not None:
                stack.append(cur)
                cur = cur.down
            else:
                node = cur.insert(num, None)
                flag = True
                while random.random() > 0.5 and flag:
                    if len(stack) > 0:
                        cur = stack.pop()
                    else:
                        flag = False
                        self.addLayer()
                        cur = self.head
                    #print(\"inserting \",num,\" to the right of \", cur.val)
                    node = cur.insert(num, node)
                break
        #self.printList()
        return False

    def erase(self, num):
        \"\"\"
        :type num: int
        :rtype: bool
        \"\"\"
        cur = self.head
        while cur is not None:
            if cur.right is None or cur.right.val > num:
                cur = cur.down
            elif cur.right.val == num:
                # expand this section
                d = cur.right
                while d is not None:
                    d.delete()
                    d = d.down
                return True
            else: # cur.next is not None and cur.next.val < target
                cur = cur.right
        return False
        


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
