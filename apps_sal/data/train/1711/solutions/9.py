class Cons:
    def __init__(self, head, tail=None):
        self.head = head
        self.tail = tail

    def to_array(self):
        return [self.head] + (self.tail.to_array() if self.tail is not None else [])

    @classmethod
    def from_array(cls, arr):
        # TODO: convert a Python list to an algebraic list.
        if len(arr) == 0:
            return None

        E = cls(arr[0])
        e = E
        for i in range(len(arr) - 1):
            e.tail = cls(arr[i + 1])
            e = e.tail
        return E

    def filter(self, fn):
        # TODO: construct new algebraic list containing only elements
        #      that satisfy the predicate.
        al = list(filter(fn, self.to_array()))
        return self.from_array(al)

    def map(self, fn):
        # TODO: construct a new algebraic list containing all elements
        #      resulting from applying the mapper function to a list.
        head, tail = self.head, self.tail
        al = list(map(fn, self.to_array()))

        return self.from_array(al)
