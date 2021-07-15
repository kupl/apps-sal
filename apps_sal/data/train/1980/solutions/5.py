class Node(object):
    
    def __init__(self, val):
        self.val = val
        self.next = None
        self.down = None

class Skiplist(object):

    def __init__(self):
        self.S = [Node(None)]

    def search(self, target):
        \"\"\"
        :type target: int
        :rtype: bool
        \"\"\"
        curr = self.S[-1]
        while curr:
            # Move right as far as possible without overshooting in the current level 
            while curr.next and (curr.next.val <= target):
                if curr.next.val == target:
                    # If target found in some (potentially intermediate) level, exit immediately
                    return True
                curr = curr.next
            # Traversed current level as far as possible without finding target
            # Move one level down to expand search
            curr = curr.down
        # Traversed till the end without finding the target, return False
        return False

    def add(self, num):
        \"\"\"
        :type num: int
        :rtype: None
        \"\"\"
        # Start at the lowest level and keep flipping coins to decide whether
        # to insert an entry for the given value at the next higher level as well.
        k = 1
        p = random.choice([0, 1])
        while (p == 1) and (k < len(self.S)):
            k += 1
            p = random.choice([0, 1])
        if k == len(self.S):
            # If an entry will be inserted at the highest level, expand the number of levels.
            nr = Node(None)
            nr.down = self.S[-1]
            self.S.append(nr)
        curr = self.S[-1]
        kc = len(self.S)
        par = None
        while curr:
            # Traverse to the right in the current level as far as possible without overshooting.
            while curr.next and (curr.next.val <= num):
                curr = curr.next
            if kc <= k:
                # An entry for the new value needs to be inserted in the current level.
                # This entry should be inserted just after the point where rightward traversal stopped.
                nn = Node(num)
                nn.next = curr.next
                curr.next = nn
                # Update the downward link for the new entry inserted in the previous level.
                if par is not None:
                    par.down = nn
                par = nn
            # Current level done, keep going down.
            curr = curr.down
            kc -= 1

    def erase(self, num):
        \"\"\"
        :type num: int
        :rtype: bool
        \"\"\"
        curr = self.S[-1]
        res = False
        while curr:
            # Traverse to the right in the current level as far as possible without overshooting.
            while curr.next and (curr.next.val <= num):
                if curr.next.val == num:
                    # Target value found inside the next node in the current level.
                    # Delete the next node, and since we're done with the current level now,
                    # break out of the loop and move on to the next level downwards.
                    res = True
                    curr.next = curr.next.next
                    break
                else:
                    curr = curr.next
            # Go one level down and repeat the process.
            curr = curr.down
        # Trim the levels if multiple levels can be found towards the top which have only the dummy terminal entry.
        # Leave only one of them.
        while len(self.S) >= 2:
            cand = self.S[-2]
            if cand.next is None:
                self.S.pop()
            else:
                break
        return res
        


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
