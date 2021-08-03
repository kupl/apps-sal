class Cons:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def to_array(self):
        return [self.head] + (self.tail.to_array() if self.tail is not None else [])

    @classmethod
    def from_array(cls, arr):
        if arr:
            return Cons(arr[0], Cons.from_array(arr[1:]) if len(arr) > 1 else None)
        return None

    def filter(self, fn):
        if self.tail:
            return Cons(self.head, self.tail.filter(fn)) if fn(self.head) else self.tail.filter(fn)
        return self if fn(self.head) else None

    def map(self, fn):
        if self.tail:
            return Cons(fn(self.head), self.tail.map(fn))
        return Cons(fn(self.head), None)
