from collections import Counter


class Node(object):
    '''
    Node of the segment tree.  

    self.val = [i,j] where i and j are lower and upper bound indices in array (arr)
    self.count = Counter(arr[i:j+1])  <-- keeps track of the frequency of each value in the range [i,j] inclusive
    '''

    def __init__(self, val):
        self.val = val
        self.count = None


class Segment_Tree(object):
    def __init__(self, arr):
        self.arr = arr
        self.root = self.build(0, len(arr) - 1)

    def build(self, i, j):
        '''
        constructs segment tree where each node has:

            1. a value of the index range [i,j] (inclusive) that it covers
            2. a counter for how many times each number appears in the range [i,j]j

        *Note, self.root will look like:

            self.root.val = [0, len(arr) - 1]
            self.root.count = Counter(arr)
        '''

        if i == j:
            node = Node([i, i])
            node.count = Counter([self.arr[i]])
            return node

        node = Node([i, j])
        k = (i + j) >> 1
        node.left = self.build(i, k)
        node.right = self.build(k + 1, j)

        node.count = node.left.count + node.right.count

        return node

    def find_most_common(self, l, r, threshold):
        '''
        returns a tuple of (most common element, frequency) in the range l, r
        where 0 <= l <= r < self.arr.length

        This is done as a subtraction process:

            1. res = self.root.count.copy()  <-- equivalent to Counter(arr)
            2. subtract values from res for ranges that are not included in l, r
            3. During this process, if the most frequent value in res ever occurs
               less than treshold times, then trigger the sentinel to quit out
            4. If a range [i,j] on the tree is completely contained within [l,r] inclusive
               then do not subtract the values in A[i:j+1] from the result
        '''

        res = self.root.count.copy()

        sentinel = False

        def helper(node):
            nonlocal res, l, r, sentinel, threshold

            if sentinel:
                return None

            if (not res) or max(res.values()) < threshold:
                sentinel = True
                res = {}
                return None

            i, j = node.val
            if (j < l) or (i > r):
                res -= node.count
                return None

            if (l <= i) and (j <= r):
                return None

            helper(node.left)
            helper(node.right)

        helper(self.root)
        most_common = max(res, key=lambda k: res[k]) if res else (-1, -1)

        return (most_common, res[most_common]) if res else most_common


class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.tree = Segment_Tree(arr)

    def query(self, left: int, right: int, threshold: int) -> int:
        val, freq = self.tree.find_most_common(left, right, threshold)
        return val if freq >= threshold else -1
