class T:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right
        
def levelorder(self):
    if not self:
        return []
    queue, R = [self], [self.value]
    while queue:
        Next = queue.pop(0)
        for T in [Next.left, Next.right]:
            if T:
                queue.append(T)
                R.append(T.value)
    return R

def is_bst1(T):
    if not (T and (T.left or T.right)):
        return True
    v, l, r = T.value, T.left, T.right
    if l and max(levelorder(l)) > v or r and min(levelorder(r)) < v:
        return False
    return is_bst1(l) and is_bst1(r)

def is_bst2(T):
    if not (T and (T.left or T.right)):
        return True
    v, l, r = T.value, T.left, T.right
    if l and min(levelorder(l)) < v or r and max(levelorder(r)) > v:
        return False
    return is_bst2(l) and is_bst2(r)

def is_bst(T):
    return is_bst1(T) or is_bst2(T)
