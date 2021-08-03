class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        self.l = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dic:
            return False
        self.l.append(val)
        self.dic[val] = len(self.l) - 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dic:
            return False
        self.dic[self.l[-1]] = self.dic[val]
        self.l[self.dic[val]], self.l[-1] = self.l[-1], self.l[self.dic[val]]
        self.l.pop()
        del self.dic[val]
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.l)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
