class Cons:

    def __init__(self, value, tail):
        self.value = value
        self.tail = tail

    def to_array(self, lst=None):
        if lst is None:
            lst = []
        lst.append(self.value)
        if self.tail is not None:
            self.tail.to_array(lst)
        return lst

    @classmethod
    def from_array(cls, arr):
        head = None
        for x in reversed(arr):
            head = Cons(x, head)
        return head

    def filter(self, fn):
        if fn(self.value):
            return Cons(self.value, self.tail and self.tail.filter(fn))
        else:
            return self.tail and self.tail.filter(fn)

    def map(self, fn):
        return Cons(fn(self.value), self.tail and self.tail.map(fn))
