class T:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

def inorder(self):
    if not self:
        return []
    return inorder(self.left) + [self.value] + inorder(self.right)

def is_bst(node):
    curr=inorder(node)
    return sorted(curr) in (curr, curr[::-1])
