class Cons:
    def __init__(self, head, tail): self.head, self.tail = head, tail
    def to_array(self): return [self.head] + (self.tail.to_array() if self.tail is not None else [])
    from_array = classmethod(lambda cls, arr, i=0, v=None: None if not arr else v if i == len(arr) else cls.from_array(arr, i + 1, Cons(arr[len(arr) - 1 - i], v)))
    def filter(self, fn): return self.from_array(list(filter(fn, self.to_array())))
    def map(self, fn): return self.from_array(list(map(fn, self.to_array())))
