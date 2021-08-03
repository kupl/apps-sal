class Node:
    def __init__(self, val):
        self.val = val        # value of the node
        self.next = None      # have next node
        self.down = None      # have down node


class Skiplist:
    def __init__(self):
        self.levels = []                    # define the levels
        prev = None                         # have previous node reference
        for i in range(16):               # 16 levels to cover the calls
            node = Node(-math.inf)          # initialize node to - infinity
            self.levels.append(node)      # append to the list growing vertically
            if prev:
                prev.down = node            # populate the down node
            prev = node                     # populate the current node as previous

    def _iter(self, val):
        res = []                                # list for the results
        l = self.levels[0]                      # start from 0th level
        while l:                              # loop from level 0 and move vertically down
            while l.next and l.next.val < val:  # as we visit each node, check if the value is lesser
                l = l.next                      # move horizontally next
            res.append(l)                     # append to the results
            l = l.down                          # move vertically down
        return res                            # return the result

    def search(self, target: int) -> bool:
        last = self._iter(target)[-1]                    # get the last element in the result after traversing for target
        return last.next and last.next.val == target     # return the element if it matches

    def add(self, num: int) -> None:
        res = self._iter(num)                            # get result as the position for num to add
        prev = None                                      # previous is None to start with
        for i in range(len(res) - 1, -1, -1):              # move from top to bottom level
            node = Node(num)                             # create Node for the value
            node.next, node.down = res[i].next, prev       # assign the next value and down value
            res[i].next = prev = node                      # assign the node to next and previous
            rand = random.random()                       # randomly decide to skip or not in each of the level
            if rand > 0.5:
                break

    def erase(self, num: int) -> bool:
        found = False                                      # found is false initially
        res = self._iter(num)                              # get the result for the number
        for i in range(len(res)):                        # iterate through the length of the results
            if res[i].next and res[i].next.val == num:     # if the value matches with levels next val
                res[i].next = res[i].next.next             # then skip the node and point to next next node
                found = True                               # set flag and return
        return found
