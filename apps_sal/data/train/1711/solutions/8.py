class Cons:

    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def to_array(self):
        return [self.head] + (self.tail.to_array() if self.tail is not None else [])

    @classmethod
    def from_array(cls, arr):
        return Cons(arr[0], Cons.from_array(arr[1:])) if arr else None

    def filter(self, fn):
        filtered_tail = None if self.tail is None else self.tail.filter(fn)
        return Cons(self.head, filtered_tail) if fn(self.head) else filtered_tail

    def map(self, fn):
        return Cons(fn(self.head), None if self.tail is None else self.tail.map(fn))
