class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        
    def __str__(self):
        if self.left or self.right:
            s = "(" + str(self.value)
            sl = self.left or '#'
            sr = self.right or '#'
            for l in str(sl).split("\n"):
                s += "\n  " + l
            for l in str(sr).split("\n"):
                s += "\n  " + l
            return s + ")"
        else:
            return f"{self.value}"

    def add(self, val):
        if val < self.value:
            if self.left:
                return self.left.add(val)
            else:
                self.left = BinaryTree(val, parent=self)
                return self.left
        elif val > self.value:
            if self.right:
                return self.right.add(val)
            else:
                self.right = BinaryTree(val, parent=self)
                return self.right
        elif val == self.value:
            return self
    
    def leftmost(self):
        x = self
        while x.left:
            x = x.left
        return x

    def nxt(self):
        if self.right:
            return self.right.leftmost().value
        else:
            x = self.parent
            while x and x.value < self.value:
                x = x.parent
            if x:
                return x.value
            
        return -1

def array_manip(array):
    if not array:
        return []
    
    result = []
    b = BinaryTree(array[-1])
    
    for item in reversed(array):
        result.append(b.add(item).nxt())
        
    return result[::-1]
    

