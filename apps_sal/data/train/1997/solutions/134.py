class Tree:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __lt__(self, other):
        if self.val[0] < other.val[0]:
            return True
        elif self.val[0] > other.val[0]:
            return False
        else:
            return self.val[1] > other.val[1]


class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        tree = Tree(val=tuple(intervals[0]))
        for (x, y) in intervals[1:]:
            this = Tree((x, y))
            cursor = tree
            while True:
                if this < cursor:
                    if cursor.left:
                        cursor = cursor.left
                    else:
                        cursor.left = this
                        break
                elif cursor < this:
                    if cursor.right:
                        cursor = cursor.right
                    else:
                        cursor.right = this
                        break
                else:
                    break
        buff = [tree]
        (count, last) = (0, None)
        while buff:
            while buff[-1].left:
                buff.append(buff[-1].left)
            while buff and (not buff[-1].right):
                this = buff.pop(-1)
                if count == 0:
                    (count, last) = (1, this.val[1])
                elif this.val[1] > last:
                    (count, last) = (count + 1, this.val[1])
            if buff:
                this = buff.pop(-1)
                if count == 0:
                    (count, last) = (1, this.val[1])
                elif this.val[1] > last:
                    (count, last) = (count + 1, this.val[1])
                buff.append(this.right)
        return count
