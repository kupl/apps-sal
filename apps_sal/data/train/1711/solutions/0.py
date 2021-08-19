class Cons:

    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def to_array(self):
        return [self.head] + (self.tail.to_array() if self.tail is not None else [])

    @classmethod
    def from_array(cls, arr):
        if not arr:
            return None
        return Cons(arr.pop(0), Cons.from_array(arr) if arr else None)

    def filter(self, fn):
        return Cons.from_array(list(filter(fn, self.to_array())))

    def map(self, fn):
        return Cons.from_array(list(map(fn, self.to_array())))
